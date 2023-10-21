from django import forms
from django.contrib.auth.models import User


class PromptForm(forms.Form):
    prompt = forms.CharField()
