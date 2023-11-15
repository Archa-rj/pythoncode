from django.contrib import admin

# Register your models here.
from .models import Office, District, Person

admin.site.register(Office)
admin.site.register(District)
admin.site.register(Person)