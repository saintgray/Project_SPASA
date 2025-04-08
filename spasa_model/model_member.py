from django.db import models

class Member(models.Model):
    id=models.CharField(max_length=15, primary_key=True)
    password=models.CharField(max_length=15)
    auth_level=models.CharField(max_length=1)
    create_by=models.CharField(max_length=20)
    create_date=models.DateField()
    update_by=models.CharField(max_length=20)
    update_date=models.DateField()
    class Meta:
        db_table='TB_SPS_C_MEMBER010'
        app_label='spasa_analyze'