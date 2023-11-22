from django.contrib.auth import get_user_model


class PublisherProxyModel(get_user_model()):
    class Meta:
        proxy = True
        verbose_name = "Publisher user"
        verbose_name_plural = "Publisher users"
