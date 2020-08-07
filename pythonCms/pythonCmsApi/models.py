from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserModel(User):
    testing = models.CharField(max_length=30, null=True)
    # websites = models.ManyToManyField(Website)
    class Meta:
        verbose_name_plural = 'user models'

class Website(models.Model):
    ownerId = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    # pages = models.ManyToManyField(Page)
    class Meta:
        verbose_name_plural = 'websites'

class Page(models.Model):
    websiteId = models.ForeignKey(Website, on_delete=models.CASCADE, null=True)
    path = models.CharField(max_length=10, null=True)
    # components = models.ManyToManyField(Component)
    class Meta:
        verbose_name_plural = 'pages'

class Component(models.Model):
    pageId = models.ForeignKey(Page, on_delete=models.CASCADE, null=True)
    fieldName = models.CharField(max_length=30, null=True)
    content = models.CharField(max_length=150, null=True)
    class Meta:
        verbose_name_plural = 'components'



        

"""
USER -< WEBSITES -< PAGES -< COMPONENTS

USER
    ID
    email
    username
    password

Website
    ID
    userId (Foreign Key)

Pages
    ID
    path
    websiteID (Foreign Key)

Components
    Id 
    componentType
    pageID (Foreign Key)

"""


