from django.contrib import admin
from .models import User,Film,Role,Review
# Register your models here.
admin.site.register(User)
admin.site.register(Film)
admin.site.register(Role)
admin.site.register(Review)