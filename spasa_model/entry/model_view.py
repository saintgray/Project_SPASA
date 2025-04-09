from django.db import models
from rest_framework import serializers

class ViewModel(models.Model):
    view_id=models.CharField(max_length=15, primary_key=True)
    view_desc=models.CharField(max_length=100)
    auth_level=models.CharField(max_length=1)
    pop_up_yn=models.CharField(max_length=1)
    create_by=models.CharField(max_length=20)
    create_date=models.DateField()
    update_by=models.CharField(max_length=20)
    update_date=models.DateField()
    class Meta:
        db_table='TB_SPS_A_VIEW010'
        app_label='spasa_analyze'
        
class View(serializers.ModelSerializer):
    class Meta:
        model=ViewModel
        fields='__all__'
        