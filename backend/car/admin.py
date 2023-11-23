from django.contrib import admin

from car.models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at", "color"]
    search_fields = ["title", "color"]
    search_help_text = "Search by title and color"
