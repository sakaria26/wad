from django.forms import ModelForm
from .models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        labels = {
            "affiliateorganisation": "Organisation"
        }
        fields = ['title', 'firstname', 'surname',
                  'email', 'password', 'affiliateorganisation']
