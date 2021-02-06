import { gql } from '@apollo/client';
import { addApolloState, initializeApollo } from 'lib/graphql/apolloClient';

export const PAGE_QUERY = gql`
    query page($contentType: String!, $token: String!) {
        page(contentType: $contentType, token: $token) {
            pageType
            id
            title
        }
    }
`;

export { default } from 'pages/[...path]';

export async function getServerSideProps({ preview, previewData }) {
    if (!preview) {
        // TODO: Serve 404 component
        return { props: {} };
    }

    const { contentType, token } = previewData;
    const apolloClient = initializeApollo();

    const props = await apolloClient.query({
        query: PAGE_QUERY,
        variables: {
            token,
            contentType,
        },
    });

    return addApolloState(apolloClient, {
        props,
    });
}
