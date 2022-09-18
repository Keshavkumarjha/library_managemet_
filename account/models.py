
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models
# Create your models here.
import uuid
TYPE_OF_USER = (
    ('student','STUDENT'),
    ('admin', 'ADMIN'),

)

class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    type = models.CharField(max_length=11, choices=TYPE_OF_USER, default='STUDENT')
class Basemodel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
       abstract = True

class Category(Basemodel):
    categori_name=models.CharField(max_length=350)

    def __str__(self):
        return self.categori_name
    
class Book(Basemodel):
    name=models.CharField(max_length=350)
    description=models.CharField(max_length=350 ,null=True,blank=True)
    author=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    book_category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='book_category')

    def __str__(self):
        return self.name
    

