from django.contrib import admin
from .models import Tip

@admin.register(Tip)
class TipAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'upvotes')
    list_filter = ('category', 'created_at')
    search_fields = ('title', 'content')
    date_hierarchy = 'created_at'
