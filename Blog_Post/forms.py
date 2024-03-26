from django import forms
from .models import UserComments


class UserCommentForm(forms.ModelForm):
    class Meta:
        model = UserComments
        fields = ['body', ]

        widgets = {
            'body': forms.Textarea(attrs={
                'class': "col-md-6 col-sm-12",
                'label': "Comment",
                "placeholder": "Message"
            })
        }
