from django.db import models
from rest_framework import serializers

class SessionModel(models.Model):
    session_key=models.CharField(max_length=40, primary_key=True)
    session_data=models.TextField(null=False)
    expire_date=models.DateTimeField()
    
    class Meta:
        db_table='DJANGO_SESSION'
        app_label='spasa_analyze'
        
class Session(serializers.ModelSerializer):
    class Meta:
        model=SessionModel
        fields='__all__'
        