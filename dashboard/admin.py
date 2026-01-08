from django.contrib import admin
from .models import TitanicPassenger


# Register your models here.
class TitanicPassengerAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "age",
        "sex",
        "fare",
        "survived",
        "embarked",
        "pclass",
    )
    list_filter = ("survived", "pclass", "embarked")
    search_fields = ("name", "sex", "embarked")


admin.site.register(TitanicPassenger, TitanicPassengerAdmin)
