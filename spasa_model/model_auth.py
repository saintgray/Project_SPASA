from django.db import models

class Auth(models.Model):
    auth_level=models.CharField(max_length=1, primary_key=True)
    auth_desc=models.CharField(max_length=100)
    class Meta:
        db_table='TB_SPS_A_AUTH010'
        app_label='spasa_analyze'