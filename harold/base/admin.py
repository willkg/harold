from django.contrib import admin
from django.core.exceptions import PermissionDenied

from harold.base.models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('created_on', 'sentiment', 'text', 'email',
                    'notes', 'assigned_to', 'closed')
    search_fields = ('text',)

    def has_add_permission(self, request, obj=None):
        # Prevent anyone from adding feedback in the admin.
        return False


admin.site.register(Feedback, FeedbackAdmin)
