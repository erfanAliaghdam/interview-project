from django.contrib.auth import get_user_model


class AuthorProxyModel(get_user_model()):
    class Meta:
        proxy = True
        verbose_name = "Author user"
        verbose_name_plural = "Author users"
