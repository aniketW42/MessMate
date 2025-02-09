from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

# Create your models here.
class mess(models.Model):
    user_id = models.ForeignKey('accounts.MessmateUser', on_delete=models.CASCADE)
    mess_name = models.CharField(max_length=50)
    loc = models.CharField(max_length=500)
    mess_owner_name = models.CharField(max_length=50)
    mess_image = models.ImageField(upload_to="images")
    mess_ratings = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], null=True)
    date_created = models.DateTimeField(default=timezone.now)