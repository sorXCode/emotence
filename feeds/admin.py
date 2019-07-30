from django.contrib import admin
from .models import *


@admin.register(Feed)
class FeedAdmin(admin.ModelAdmin):
    
    search_fields = ('emtex',)
