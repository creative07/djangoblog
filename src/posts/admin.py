from django.contrib import admin
from .models import post


class postModelAdmin(admin.ModelAdmin):
    list_display = ["title","updated","timestamp"]
    list_editable=["title"]
    list_display_links = ["updated"]
    list_filter = ["updated","timestamp"]
    search_fields = ["title","content"]
    class Meta:
        model = post




admin.site.register(post, postModelAdmin)

