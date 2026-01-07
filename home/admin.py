from django.contrib import admin
from .models import Colors, Person , PersonDetail, Students

# Register your models here.
admin.site.register(Colors)
admin.site.register(Person)
admin.site.register(PersonDetail)
admin.site.register(Students)