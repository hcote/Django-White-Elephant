from django.contrib import admin

# Register your models here.
from .models import Categories 

# Categories will now show up in admin backend where you can add posts
admin.site.register(Categories)