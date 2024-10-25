from django.forms import ModelForm
from .models import upper
class signupform(ModelForm):
    class Meta:
        model = upper
        fields = "__all__"