from django.contrib import admin
from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    
    list_display = ["__str__", "last_updated"]
    readonly_fields = ["id","last_updated"]
    list_filter = ["title", "last_updated"]
    search_fields = ["title"]
    class Meta:
        model = Review

admin.site.register(Review, ReviewAdmin)
