from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.IntegerField(primary_key=True, db_column='User ID')
    user_name = models.CharField(max_length=50, db_column='User Name')
    user_age = models.IntegerField(db_column='Age')
    user_email = models.EmailField(max_length=50, db_column = 'Email')
    user_phone = models.CharField(max_length=20, db_column='Phone')
    user_address = models.CharField(max_length=50, db_column='Address')

    class Meta:
        db_table = 'User-info'
