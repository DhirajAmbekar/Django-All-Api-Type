from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name


class Blog(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to="images/", null= True,blank=True)
    user = models.ManyToManyField(User, null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    updated_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
