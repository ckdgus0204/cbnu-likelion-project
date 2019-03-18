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

def get_image_filename(instance, filename):
    id = instance.post.id
    return "post_images/%s" % (id) 

class Images(models.Model):
    image = models.ImageField(upload_to=get_image_filename, verbose_name='Image') 

class Comment(models.Model):
    recomment = models.ForeignKey("self", on_delete=models.SET_NULL, null=True)
    text = models.CharField(max_length=100)

class Product(Base):
    pass

class Book(Base):
    edition = models.CharField(max_length=5)
    author = models.CharField(max_length=10)

class Room(Base):
    position = models.CharField(max_length=100)

class ProductComment(Comment):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)

class BookComment(Comment):
    book = models.ForeignKey(Book, default=None, on_delete=models.CASCADE)

class RoomComment(Comment):
    room = models.ForeignKey(Room, default=None, on_delete=models.CASCADE)

class ProductImages(Images):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)

class BookImages(Images):
    book = models.ForeignKey(Book, default=None, on_delete=models.CASCADE)

class RoomImages(Images):
    room = models.ForeignKey(Room, default=None, on_delete=models.CASCADE)


