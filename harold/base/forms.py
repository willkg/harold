from django import forms
from django.utils.translation import ugettext as _

from harold.base import config


class FeedbackForm(forms.Form):
    """Basic response feedback form."""
    text = forms.CharField(widget=forms.Textarea(), required=True)
    sentiment = forms.ChoiceField(choices=config.SENTIMENT_CHOICES, required=True)
    email = forms.EmailField(required=False)
