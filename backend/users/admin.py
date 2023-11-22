from django.contrib import admin
from django.contrib.auth import get_user_model
from users.adminsites import (
    ClientUserAdmin,
    AdminUserAdmin,
)
from users.models.proxy import (
    ClientProxyModel,
    AdminProxyModel,
)

admin.site.register(get_user_model())
admin.site.register(ClientProxyModel, ClientUserAdmin)
admin.site.register(AdminProxyModel, AdminUserAdmin)

