from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

class Material(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200, blank=True, null=True)
    def __str__(self):
        return self.name

class Size(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    size = models.ManyToManyField(Size)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, blank=True, null=True)
    color = models.ManyToManyField(Color)
    def __str__(self):
        return self.name

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField()             # Оценка
    comment = models.CharField(max_length=300)



