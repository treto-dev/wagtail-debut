import querystring from 'querystring';
import { getPage, getRedirect, getAllPages } from 'lib/api/wagtail';
import { gql, useQuery } from '@apollo/client';
import dynamic from 'next/dynamic';

export const PAGE_SUBSCRIPTION = gql`
    subscription page($contentType: String!, $token: String!) {
        page(contentType: $contentType, token: $token) {
            pageType
            id
            title
        }
    }
`;

const isProd = process.env.NODE_ENV === 'production';

export default function CatchAllPreviewPage({
    componentName,
    contentType,
    token,
}) {
    // Basic
    const { loading, error, data } = useSubscription(PAGE_SUBSCRIPTION, {
        variables: {
            token,
            contentType,
        },
    });

    if (loading) {
        return <>loading</>;
    }

    if (data?.page?.pageType) {
        const Component = dynamic(
            () => import(`containers/${data.page.pageType}`)
        );
        return <Component {...data.page} />;
    }

    return <h1>Component {componentName} not found</h1>;
}

// For SSR
export async function getServerSideProps({ req, preview, previewData }) {
    if (!preview) {
        // TODO: Serve 404 component
        return { props: {} };
    }

    const { contentType, token, host } = previewData;
}
