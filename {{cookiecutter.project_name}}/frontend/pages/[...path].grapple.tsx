import querystring from 'querystring';
import { gql, useQuery } from '@apollo/client';
import { addApolloState, initializeApollo } from 'lib/graphql/apolloClient';
import dynamic from 'next/dynamic';

export const PAGE_QUERY = gql`
    query page($urlPath: String!) {
        page(urlPath: $urlPath) {
            pageType
            id
            title
            seoTitle
            searchDescription
        }
    }
`;

const isProd = process.env.NODE_ENV === 'production';

export default function CatchAllPage({ componentName, data, loading, error }) {
    if (loading) {
        return <>Loading</>;
    }

    if (error) {
        console.error(error);
    }

    if (data?.page?.pageType) {
        const Component = dynamic(
            () => import(`containers/${data.page.pageType}`)
        );
        /**
         * FIXME: The seo props below is mainly used to provide backward compatibility with
         * Wagtail-Pipit.
         *
         * Dropping default Wagtail-Pipit support would require renaming the props used in
         * containers/BasePage/BasePage.tsx.
         */
        return (
            <Component
                {...data.page}
                seo={{
                    seoHtmlTitle: data.page.seoTitle,
                    seoMetaDescription: data.page.searchDescription,
                    seoOgDescription: data.page.searchDescription,
                }}
            />
        );
    }

    return <h1>Component {componentName} not found</h1>;
}

export async function getServerSideProps({ req, params, res }) {
    const path = params?.path.join('/') || '/';

    // TODO: Reuse or remove code below
    const { host } = req.headers;
    let queryParams = new URL(req.url, `https://${host}`).search;
    if (queryParams.indexOf('?') === 0) {
        queryParams = queryParams.substr(1);
    }

    const parsedQueryParams = querystring.parse(queryParams);

    const apolloClient = initializeApollo();

    const props = await apolloClient.query({
        query: PAGE_QUERY,
        variables: {
            urlPath: path,
        },
    });

    return addApolloState(apolloClient, {
        props,
    });
}
