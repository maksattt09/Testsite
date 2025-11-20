from django.db import models
from phonenumber_field.modelfields import PhoneNumberField



class Category(models.Model):
    category_name = models.CharField(max_length=30, unique=True)
    category_image = models.ImageField(upload_to='cate_images/')

    def __str__(self):
        return f'Название: {self.category_name}'


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    owner = models.CharField(max_length=50)
    phone_number = PhoneNumberField()
    product_image = models.ImageField(upload_to='product_photo')
    product_type = models.BooleanField(default=False)
    description = models.TextField()
    created_date = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.product_name
