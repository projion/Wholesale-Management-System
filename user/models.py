from django.db import models
# Create your models here.
class User(models.Model):
    # user_id = models.IntegerField(primary_key=True, db_column='User ID')
    username = models.CharField(max_length=50, db_column='User Name', unique=True)
    password = models.CharField(max_length=500, db_column='Password')
    firstname= models.CharField(max_length=20, db_column='First Name')
    lastname = models.CharField(max_length=20, db_column='Last Name')
    user_age = models.IntegerField(db_column='Age')
    user_email = models.EmailField(unique=True)
    user_phone = models.CharField(max_length=20, db_column='Phone')
    user_address = models.CharField(max_length=50, db_column='Address')
    user_type = models.CharField(max_length=20, db_column='User Type')
    profile_photo= models.ImageField(upload_to='images/')

    class Meta:
        db_table = 'User-info'

    @staticmethod
    def get_user_by_mail(usesdcar_email):
        try:
            return User.objects.get(user_email=usesdcar_email)
        except:
            return False