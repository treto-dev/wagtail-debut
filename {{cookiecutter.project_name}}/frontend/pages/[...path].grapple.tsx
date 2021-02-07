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

const ALL_PAGES_QUERY = gql`
    query allPages {
        pages {
            id
            urlPath
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
         * FIXME: The seo props below are mainly used to provide backward compatibility with
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

export async function getStaticPaths() {
    const apolloClient = initializeApollo();

    const { data } = await apolloClient.query({
        query: ALL_PAGES_QUERY,
        variables: {
            urlPath: path,
        },
    });
    return {
        paths: data.pages.map(({ id, urlPath }) => ({
            params: { id, urlPath },
        })),
        fallback: true,
    };
}

export async function getStaticProps({ params }) {
    const path = params?.path.join('/') || '/';

    const apolloClient = initializeApollo();

    const props = await apolloClient.query({
        query: PAGE_QUERY,
        variables: {
            urlPath: path,
        },
    });

    return {
        ...addApolloState(apolloClient, {
            props,
        }),
        revalidate: 1,
    };
}
