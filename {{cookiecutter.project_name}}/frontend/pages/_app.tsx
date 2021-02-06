import * as Sentry from '@sentry/node';
import { ApolloProvider } from '@apollo/client';
import { RewriteFrames } from '@sentry/integrations';
import getConfig from 'next/config';
import { useApollo } from 'lib/graphql/apolloClient';
import '../index.css';

if (process.env.NEXT_PUBLIC_SENTRY_DSN) {
    const config = getConfig();
    const distDir = `${config.serverRuntimeConfig.rootDir}/.next`;
    Sentry.init({
        enabled: process.env.NODE_ENV === 'production',
        integrations: [
            new RewriteFrames({
                iteratee: (frame) => {
                    frame.filename = frame.filename.replace(
                        distDir,
                        'app:///_next'
                    );
                    return frame;
                },
            }),
        ],
        dsn: process.env.NEXT_PUBLIC_SENTRY_DSN,
    });
}

function MyApp({ Component, pageProps, err }) {
    const apolloClient = useApollo(pageProps);
    return (
        <ApolloProvider client={apolloClient}>
            <Component {...pageProps} err={err} />
        </ApolloProvider>
    );
}

export default MyApp;
