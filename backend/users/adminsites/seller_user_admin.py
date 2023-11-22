from django.contrib.auth.admin import UserAdmin


class SellerUserAdmin(UserAdmin):
    list_display = (
        'email',
        'first_name',
        'last_name',
        'user_identifier',
        'is_active'
    )
    ordering = ["date_joined"]
    list_filter = [
        'is_active',
        'date_joined'
    ]
    search_fields = ["email", "first_name", "last_name", "user_identifier"]
    search_help_text = "search by : email, first name, last name, user identifier"

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(groups__name="Sale")