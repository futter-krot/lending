from django.db import models
# Create your models here.
class Author(models.Model):  
    full_name = models.TextField()  
    birth_year = models.SmallIntegerField()  
    country = models.CharField(max_length=2)
    def __str__(self):
        return self.full_name
class Redaction(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name

class Book(models.Model):  
    ISBN = models.CharField(max_length=13)  
    title = models.TextField()  
    description = models.TextField()  
    year_release = models.SmallIntegerField()  
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    copy_count = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    redaction = models.ForeignKey(Redaction, on_delete=models.CASCADE, null=True, blank=True, related_name='books')
    def __str__(self):
        return self.title
class Friend(models.Model):
    name = models.CharField(max_length=128)
    lent = models.ManyToManyField(Book, null=True, blank=True)
    def __str__(self):
        return self.lent