# Wagtail Début

Wagtail Début is a [Wagtail CMS](https://wagtail.io/) boilerplate which aims to provide an easy and modern developer workflow with a React-rendered frontend.  
It is based on [Wagtail Pipit](https://github.com/Frojd/Wagtail-Pipit) but is less opiniated, and let you choose between a standard Wagtail app or a headless app.  
It also provides the choice between a standard DRF based headless wagtail, or a [Wagtail Grapple](https://github.com/GrappleGQL/wagtail-grapple) bashed headless wagtail.

## Features

- Page scaffolding
- [12-Factor App](https://12factor.net/) compliant
- Docker development environment
- Data-sync between environments

### Optionnal features

#### Decoupled frontend
- Hybrid static and server rendered React using [Next.js](https://nextjs.org/)
- [Storybook](https://storybook.js.org/) for rapid React component development
- DRF-based or [Wagtail Grapple](https://github.com/GrappleGQL/wagtail-grapple) based

#### Standard django frontend
- [Django Pattern Library](https://github.com/torchbox/django-pattern-library) for rapid Django component development

#### Deployment / CI/CD
- Deploy scripts via [Ansistrano](https://github.com/ansistrano)
- Orchestration using [Ansible](https://github.com/ansible/ansible)
- Error reporting with [Sentry](https://sentry.io/)
- CI integration via [Circle CI](https://circleci.com/)
> - Local SSL for development

## Installation

1. Make sure you have [cookiecutter](https://github.com/audreyr/cookiecutter/blob/master/docs/index.rst) installed. If not run `pip install cookiecutter` (or via brew)
2. Run cookiecutter:

```
cookiecutter https://github.com/l-etabli/wagtail-debut.git
```

3. Fill in the questions and you are done!

## Documentation – Where to go from here?

We recommend you to start by checking out the [Getting Started Guide](/docs/getting-started-guide.md). Otherwise, you can read up any of the following topics:

- [Frontend Developer Guide](/docs/frontend-developer-guide.md)
- [Backend Developer Guide](/docs/backend-developer-guide.md)
- [Datasync between environments](/docs/data-sync.md)
- [Scaffolding](/docs/scaffolding.md)
- [Deploying with Ansistrano](/docs/deployment.md)
- [Setting up continuous integration on CircleCI](/docs/ci.md)
- [Running python locally](/docs/running-python-locally.md)
- [Using static site generation](/docs/using-static-site-generation.md)
- [Working with Wagtail's routable pages](/docs/working-with-wagtails-routable-pages.md)
- [Serving custom content type data through Next.js](/docs/serving-custom-content-type-data-through-nextjs.md)
- [Adding multi language support](/docs/adding-multi-language-support.md)

## Contribute

If you have ideas for improvement, please share your thoughts through an issue. We also welcome PR's

- Issue Tracker: [https://github.com/l-etabli/wagtail-debut/issues](https://github.com/l-etabli/wagtail-debut/issues)
- Source Code: [https://github.com/l-etabli/wagtail-debut](https://github.com/l-etabli/wagtail-debut)
- Discussions: You can find us on the [Wagtail slack](https://wagtail.io/slack/) under the channel `#pipit`

## Security

If you believe you have found a security issue with any of our projects please email us at [security@letabli.io](security@letabli.io).

## Support

If you have any issues, please submit an issue and we will do our best to help you out.
