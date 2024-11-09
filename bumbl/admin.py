from django.contrib import admin

from .models import Comment, Entry, File, RawEntry, Redirect, Tag


class EntryAdmin(admin.ModelAdmin):
    exclude = (
        "path",
        "total_css",
        "total_section_content",
    )


admin.site.register(Entry, EntryAdmin)
admin.site.register(Tag)
admin.site.register(File)
admin.site.register(Comment)
admin.site.register(Redirect)
admin.site.register(RawEntry)
