# Generated by Django 3.1.7 on 2021-04-02 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
