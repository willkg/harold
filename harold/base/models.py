from datetime import datetime

from django.contrib.auth.models import User
from django.db import models

from rest_framework import serializers


class Feedback(models.Model):
    sentiment = models.CharField(max_length=10)
    text = models.TextField(blank=True)
    email = models.EmailField(blank=True)

    created_on = models.DateTimeField(default=datetime.now)
    notes = models.TextField(blank=True, default=u'')
    assigned_to = models.ForeignKey(User, null=True)
    closed = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def save(self, *args, **kwargs):
        if not self.email:
            self.closed = True

        super(Feedback, self).save(*args, **kwargs)


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback

        # We only want to include fields that don't have private data
        # in them.
        fields = ('sentiment', 'text', 'created_on')
        write_only_fields = ('email',)
