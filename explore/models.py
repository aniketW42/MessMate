from django.db import models
from mess_owner.models import mess
# Create your models here.

class mess_menu(models.Model):
    mess_id = models.OneToOneField(mess, on_delete=models.SET_NULL, null=True)
    menu = models.TextField(null=False)
    from_time = models.TimeField(default='00:00')
    to_time = models.TimeField(default='00:00')
