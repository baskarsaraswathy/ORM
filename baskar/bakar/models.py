from django.db import models
from django.contrib import admin
class football_player(models.Model):
   p_regno=models.IntegerField()
   p_name=models.CharField(max_length=20)
   p_age=models.IntegerField()
   p_country=models.CharField(max_length=20)
   p_email=models.EmailField()
   
class football_playerAdmin(admin.ModelAdmin):   
   list_display=('p_regno','p_name','p_age','p_country','p_email')
