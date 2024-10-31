from django.contrib import admin
from .models import Frontend, Backend,Project


admin.site.register(Backend)
admin.site.register(Frontend)
admin.site.register(Project)