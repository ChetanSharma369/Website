from django.contrib import admin
from .models import Colors, Person , PersonDetail

# Register your models here.
admin.site.register(Colors)
admin.site.register(Person)
admin.site.register(PersonDetail)