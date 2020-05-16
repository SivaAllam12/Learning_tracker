from django.contrib import admin
from .models import Course
from .models import Entry

admin.site.register(Course)
admin.site.register(Entry)

