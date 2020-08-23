from django.contrib import admin
from .models import Person

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    model = Person
    list_display = ("id", "name", "gender", "dob", "blood_type", "height", "weight")

