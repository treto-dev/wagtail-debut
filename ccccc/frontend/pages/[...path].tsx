import querystring from 'querystring';
import { getPage, getRedirect, getAllPages } from 'lib/api/wagtail';
import { gql, useQuery } from '@apollo/client';
import dynamic from 'next/dynamic';

export const PAGE_QUERY = gql`
    query page($urlPath: String!) {
        page(urlPath: $urlPath) {
            pageType
            id
            title
        }
    }
`;

const isProd = process.env.NODE_ENV === 'production';

export default function CatchAllPage({ componentName, path }) {
    // Basic
    const { loading, error, data } = useQuery(PAGE_QUERY, {
        variables: {
            urlPath: path,
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

export async function getServerSideProps({ req, params, res }) {
    const path = params?.path.join('/') || '/';
    return { props: { path } };

    // TODO: Reuse or remove code below
    const { host } = req.headers;
    let queryParams = new URL(req.url, `https://${host}`).search;
    if (queryParams.indexOf('?') === 0) {
        queryParams = queryParams.substr(1);
    }
    const parsedQueryParams = querystring.parse(queryParams);
}

// For SSG
/*
export async function getStaticProps({ params, preview, previewData }) {
params = params || {};
let path = params.path || [];
path = path.join("/");

const pageData = await getPage(path);
return { props: pageData }
}

export async function getStaticPaths() {
const data = await getAllPages();

let htmlUrls = data.items.map(x => x.relativeUrl);
htmlUrls = htmlUrls.filter(x => x);
htmlUrls = htmlUrls.map(x => x.split("/"));
htmlUrls = htmlUrls.map(x => x.filter(y => y))
htmlUrls = htmlUrls.filter(x => x.length)

const paths = htmlUrls.map(x => (
{ params: { path: x } }
));

return {
paths: paths,
fallback: false,
};
}
*/

// For SSG
/*
export async function getStaticProps({ params, preview, previewData }) {
params = params || {};
let path = params.path || [];
path = path.join("/");

const pageData = await getPage(path);
return { props: pageData }
}

export async function getStaticPaths() {
const data = await getAllPages();

let htmlUrls = data.items.map(x => x.relativeUrl);
htmlUrls = htmlUrls.filter(x => x);
htmlUrls = htmlUrls.map(x => x.split("/"));
htmlUrls = htmlUrls.map(x => x.filter(y => y))
htmlUrls = htmlUrls.filter(x => x.length)

const paths = htmlUrls.map(x => (
{ params: { path: x } }
));

return {
paths: paths,
fallback: false,
};
}
*/
