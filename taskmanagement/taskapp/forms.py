from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Team, Task
from django.forms import ModelForm


# Create your forms here.

class DateInput(forms.DateInput):
    input_type = 'date'


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class TeamForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Team
        fields = "__all__"

#id, name, team, team members, status, started_at, completed_at)
class TaskForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            'started_at': DateInput(),
            'completed_at': DateInput(),
        }
