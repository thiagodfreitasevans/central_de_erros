from rest_framework import serializers
from . import models

class LogSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default = serializers.CurrentUserDefault()
    )
        
    class Meta:
        model = models.Log
        fields = (
            "title",
            "details",
            "events",
            "env",
            "level",
            "origin",
            "owner",
            "archived"
        )