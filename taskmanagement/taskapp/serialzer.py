from rest_framework import serializers
from .models import User, Team, Task

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'