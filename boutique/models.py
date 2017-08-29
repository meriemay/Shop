from django.contrib.auth.models import Permission, User
from django.db import models
from django.conf import settings
from django.utils import timezone





class Commercant(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    name = models.CharField(max_length=250, default=None)
    description = models.TextField(max_length=250, default=None)
    tel = models.IntegerField(default=None)
    picture = models.ImageField()

    def __str__(self):
        return self.name



class Shop(models.Model):
    user = models.ForeignKey(User, default=1)
    username = models.CharField(max_length=250)
    shop_name = models.CharField(max_length=500)
    shop_logo = models.FileField(null=True)
    is_favorite = models.BooleanField(default=False)
    visitors = models.ManyToManyField(User,related_name='user')
    Msg_Parametre = models.TextField(default='Can I help you?')

    def __str__(self):
        return self.shop_name + ' - ' + self.username


class Category(models.Model):
    label = models.CharField(
        max_length=250, 
        unique=True 
    )

    def __str__(self):
        return self.label



def user_directory_path(instance, filename):
    return 'user_{0}/{1}/{2}'.format(instance.shop.user.username, instance.shop.shop_name, str(timezone.now)+str(filename))


class Product(models.Model):

    Hand_Made = 'Hand_Made'
    Vintage = 'Vintage'
    Baby = 'Baby'
    Child = 'Child'
    Teenager = 'Teenager'
    Adult = 'Adult'
    Male = 'Male'
    Female = 'Female'
            

    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=250)
    product_price = models.FloatField()  
    product_logo = models.ImageField(null=True, upload_to=user_directory_path)
    product_pic1 = models.ImageField(null=True, upload_to=user_directory_path)
    product_pic2 = models.ImageField(null=True, upload_to=user_directory_path)
    product_pic3 = models.ImageField(null=True, upload_to=user_directory_path)
    is_activate = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None,
        blank=True)
    product_type = models.CharField(
        max_length=20,
        blank=True,
        choices=(
            (Hand_Made, 'Hand_Made'),
            (Vintage, 'Vintage')
        ),default=None
    )
    gender = models.CharField(
        max_length=15,
        blank=True,
        choices=(
            (Male, 'Male'),
            (Female, 'Female')
        ),default=None
    )
    age = models.CharField(
        max_length=10,
        blank=True,
        choices=(
            (Baby, 'Baby'),
            (Child, 'Child'),
            (Teenager, 'Teenager'),
            (Adult, 'Adult')
        ),default=None
    )
    description = models.TextField(max_length=250, default=None)
    quantite = models.IntegerField(default=None)
    date = models.DateField(auto_now_add=True, null=True)
    tags = models.TextField(max_length=250, blank=True, default=None,null=True)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.product_name

    class Meta:
        ordering = ('-date',)


class Wishlist(models.Model):
    user = models.ForeignKey(User)
    product = models.ManyToManyField(Product,blank=True, null=True)
    name = models.CharField(max_length=250, default=None)

    def __str__(self):
        return self.name

class Picture(models.Model):
    product = models.ForeignKey(Product)
    name = models.ImageField(blank=True,null=True)





        


