from django.urls import path
from . import views as product_view


urlpatterns = [
    path('details/', product_view.product1, name='product-details'),

]