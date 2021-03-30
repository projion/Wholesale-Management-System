# Generated by Django 3.1.7 on 2021-03-29 05:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20210329_1054'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.IntegerField(db_column='Product ID', primary_key=True, serialize=False)),
                ('product_name', models.CharField(db_column='Product Name', max_length=50)),
                ('price', models.IntegerField(db_column='Price')),
                ('status', models.BooleanField(db_column='Status', default=False)),
                ('quantity', models.IntegerField(db_column='Quantity')),
                ('category_id', models.ForeignKey(db_column='Category ID', on_delete=django.db.models.deletion.CASCADE, to='product.category')),
            ],
            options={
                'db_table': 'Product-info',
            },
        ),
    ]
