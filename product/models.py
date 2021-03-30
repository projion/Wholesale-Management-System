from django.db import models

# Create your models here.
class Category(models.Model):
    category_id = models.IntegerField(primary_key=True, db_column='Category ID')
    category_name = models.CharField(max_length=50, db_column='Category Name')

    class Meta:
        db_table = 'Category'

class Product(models.Model):
    product_id = models.IntegerField(primary_key=True, db_column='Product ID')
    product_name = models.CharField(max_length=50, db_column='Product Name')
    price = models.IntegerField(db_column='Price')
    status = models.BooleanField(default=False, db_column='Status')
    quantity = models.IntegerField( db_column='Quantity')
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, db_column='Category ID')

    class Meta:
        db_table = 'Product-info'

