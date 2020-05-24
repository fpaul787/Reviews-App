from django.contrib import admin
from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    
    list_display = ["__str__", "last_updated"]
    readonly_fields = ["last_updated"]
    class Meta:
        model = Review

admin.site.register(Review, ReviewAdmin)
