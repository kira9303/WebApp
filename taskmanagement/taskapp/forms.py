from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Team, Task

from django.db import models
from django.forms import ModelForm


# Create your forms here.

'''user = "USER"
team_leader = "TEAM_LEADER"
team_member = "TEAM_MEMBER"


status_choice = (
    (user, "user"),
    (team_leader, "team_leader"),
    (team_member, "team_member"),
    # ....
)'''

USER_ROLES =(
    ("1", "User"),
    ("2", "Team Leader"),
    ("3", "Team Member"),

)

'''class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = '__all__'

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.status = self.cleaned_data['status']
        if commit:
            user.save()
        return user'''


class DateInput(forms.DateInput):
    input_type = 'date'


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    #status = forms.CharField(max_length=30, choices=status_choice, default="USER")
    status = forms.ChoiceField(choices=USER_ROLES)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "status")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.status = self.cleaned_data['status']
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
