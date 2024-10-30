from django.forms import ModelForm
from .models import just_log
class signupform(ModelForm):
    class Meta:
        model = just_log
        fields = "__all__"
    print('form_section')