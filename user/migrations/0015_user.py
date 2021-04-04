# Generated by Django 3.1.7 on 2021-04-04 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0014_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(db_column='User Name', max_length=50, unique=True)),
                ('password', models.CharField(db_column='Password', max_length=500)),
                ('firstname', models.CharField(db_column='First Name', max_length=20)),
                ('lastname', models.CharField(db_column='Last Name', max_length=20)),
                ('user_age', models.IntegerField(db_column='Age')),
                ('user_email', models.EmailField(max_length=254, unique=True)),
                ('user_phone', models.CharField(db_column='Phone', max_length=20)),
                ('user_address', models.CharField(db_column='Address', max_length=50)),
                ('user_type', models.CharField(db_column='User Type', max_length=20)),
                ('profile_photo', models.ImageField(upload_to='static/media')),
            ],
            options={
                'db_table': 'User-info',
            },
        ),
    ]
