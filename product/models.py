from django.db import models

# Create your models here.
class Category(models.Model):
    # category_id = models.IntegerField(primary_key=True, db_column='Category ID')
    category_name = models.CharField(primary_key=True, max_length=100, db_column='Category Name')

    class Meta:
        db_table = 'Category'
    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_id = models.IntegerField(primary_key=True, db_column='Product ID')
    product_name = models.CharField(max_length=50, db_column='Product Name')
    price = models.IntegerField(db_column='Price')
    status = models.BooleanField(default=False, db_column='Status')
    quantity = models.IntegerField( db_column='Quantity')
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE, db_column='Category ID')

    class Meta:
        db_table = 'ProductInfo'

    @staticmethod
    def get_product_by_id(category_name):
        try:
            return Product.objects.get(category_name=category_name)
        except:
            return False

    @staticmethod
    def get_product_by_name(product_name):
        try:
            return Product.objects.get(product_name=product_name)
        except:
            return False

