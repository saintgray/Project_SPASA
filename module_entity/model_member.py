from django.db import models
from django.http import HttpRequest
from rest_framework import serializers
from datetime import datetime
import json

class MemberModel(models.Model):
        
    id=models.CharField(max_length=15, primary_key=True)
    password=models.CharField(max_length=15)
    auth_level=models.CharField(max_length=1)
    create_by=models.CharField(max_length=20)
    create_date=models.DateTimeField()
    update_by=models.CharField(max_length=20)
    update_date=models.DateTimeField()
    
    class Meta:
        db_table='TB_SPS_C_MEMBER010'
        app_label='spasa_analyze'

class Member(serializers.ModelSerializer):
    class Meta:
        model=MemberModel
        fields='__all__'