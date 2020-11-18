from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Login(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    logged_in = models.BooleanField(default=False)

    def __str__(self):
        return (str(self.user.username)+"-"+str(self.logged_in))
        



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Login.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.login.save()


class Product(models.Model):
    product_name = models.CharField(max_length=350)
    product_details = models.TextField()
    product_img = models.ImageField(null=True, blank=True, upload_to="images/")
    product_link = models.CharField(
        max_length=500, blank=True, null=True)
    product_download = models.FileField(
        null=True, blank=True, upload_to="products/")
    price = models.IntegerField()

    def __str__(self):
        return self.product_name


class Purchase(models.Model):
    purchased_by = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.purchased_by.username + "-" + self.product.product_name

class Getting_Started_Section(models.Model):
    Section = models.CharField(max_length=350,unique=True)
    def __str__(self):
        return self.Section

class Getting_Started_Affiliate_Link(models.Model):
    Section_Name = models.ForeignKey(Getting_Started_Section, on_delete=models.CASCADE) 
    Display_Name=models.CharField(max_length=500,null=True, blank=True)
    Affiliate_Link = models.CharField(max_length=500, blank=True, null=True,unique=True)

    def __str__(self):
        Str = self.Affiliate_Link.split("/")[2]
        return Str+ " , " +self.Section_Name.Section if Str.startswith("www.") else "www."+Str + " , " +self.Section_Name.Section

class Model_Content_Section(models.Model):
    Section = models.CharField(max_length=350,unique=True)
    def __str__(self):
        return self.Section

class Model_Content_Affiliate_Link(models.Model):
    Section_Name = models.ForeignKey(Model_Content_Section, on_delete=models.CASCADE) 
    Display_Name=models.CharField(max_length=500,null=True, blank=True,unique=True)
    Affiliate_Link = models.CharField(max_length=500, blank=True, null=True,unique=True)

    def __str__(self):
        Str = self.Affiliate_Link.split("/")[2]
        return Str+ " , " +self.Section_Name.Section if Str.startswith("www.") else "www."+Str + " , " +self.Section_Name.Section

class Customize_Content_Section(models.Model):
    Section = models.CharField(max_length=350,unique=True)
    def __str__(self):
        return self.Section

class Customize_Content_Affiliate_Link(models.Model):
    Section_Name = models.ForeignKey(Customize_Content_Section, on_delete=models.CASCADE) 
    Display_Name=models.CharField(max_length=500,null=True, blank=True)
    Affiliate_Link = models.CharField(max_length=500, blank=True, null=True,unique=True)
    
    def __str__(self):
        Str = self.Affiliate_Link.split("/")[2]
        return Str+ " , " +self.Section_Name.Section if Str.startswith("www.") else "www."+Str + " , " +self.Section_Name.Section

class Publish_Section(models.Model):
    Section = models.CharField(max_length=350,unique=True)
    def __str__(self):
        return self.Section

class Publish_Affiliate_Link(models.Model):
    Section_Name = models.ForeignKey(Publish_Section, on_delete=models.CASCADE) 
    Display_Name=models.CharField(max_length=500,null=True, blank=True)
    Affiliate_Link = models.CharField(max_length=500, blank=True, null=True,unique=True)
    def __str__(self):
        Str = self.Affiliate_Link.split("/")[2]
        return Str+ " , " +self.Section_Name.Section if Str.startswith("www.") else "www."+Str + " , " +self.Section_Name.Section

class Resources_Section(models.Model):
    Section = models.CharField(max_length=350,unique=True)
    def __str__(self):
        return self.Section

class Resources_Affiliate_Link(models.Model):
    Section_Name = models.ForeignKey(Resources_Section, on_delete=models.CASCADE) 
    Display_Name=models.CharField(max_length=500,null=True, blank=True)
    Affiliate_Link = models.CharField(max_length=500, blank=True, null=True,unique=True)
    def __str__(self):
        Str = self.Affiliate_Link.split("/")[2]
        return Str+ " , " +self.Section_Name.Section if Str.startswith("www.") else "www."+Str + " , " +self.Section_Name.Section