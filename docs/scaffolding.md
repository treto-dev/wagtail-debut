# Scaffolding

We provide a scaffolding management command to make it easier
for you to create the neccessary files for a new page.

If you run:

```sh
./scripts/manage.sh new_page --name=Article
```

The following files will be created for you with some default code in them:

* wagtail/project_name/pages/article.py
* wagtail/project_name/pages/article_serializer.py
* wagtail/project_name/tests/test_article_page.py
* wagtail/project_name/factories/article_page.py
