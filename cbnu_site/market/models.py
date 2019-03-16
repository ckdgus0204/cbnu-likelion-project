from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Base(models.Model):
    price = models.IntegerField()
    image = models.FileField()
    title = models.CharField(max_length=100)
    text = models.TextField()
    status_content = models.CharField(max_length=100)
    number = models.CharField(max_length=20)
    soldout = models.BooleanField(default=False)

class Images(models.Model):

class Comment(models.Model):
    recomment = models.ForeignKey("self")
    text = models.CharField(max_length=100)

class Product(Base):

class Book(Base):
    edition = models.CharField(max_length=5)
    author = models.CharField(max_length=10)

class Room(Base):
    position = models.CharField(max_length=100)

class ProductComment(Comment):
    product = models.ForeignKey()

class BookComment(Comment):
    book = models.ForeignKey()

class RoomComment(Comment):
    room = models.ForeignKey()


