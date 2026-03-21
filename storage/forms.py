from django import forms
from django.contrib.auth import get_user_model

# Models
from users.models import Notification

User = get_user_model()


class MessageForm(forms.ModelForm):
    sent_to = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=forms.Select(attrs={
            'class': ""
        }),
        empty_label=None
    )
    
    class Meta:
        model = Notification
        fields = ['msg_text', 'sent_to']
        widgets = {
            'msg_text': forms.Textarea(attrs={
                'class': "w-full max-w-sm bg-stone-800 hover:bg-stone-700 rounded-md p-2 shadow-md outline-none text-sm"
            })
        }