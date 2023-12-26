from django.db import models
import datetime


YEAR_CHOICES = []
for r in range(1980, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r,r))


# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name =  models.CharField(max_length=50)
    
    
class Publisher(models.Model):
    publisher = models.CharField(max_length=50)
    location =  models.CharField(max_length=100)
    
    
class Langauge(models.Model):
    langauge = models.CharField(max_length=50)
    

class Category(models.Model):
    category = models.CharField(max_length=50)
    category_persian = models.CharField(max_length=100)
    
    
class Section(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    section = models.CharField(max_length=50)
    section_persian = models.CharField(max_length=100)
    
    
class Faculty(models.Model):
    faculty = models.CharField(max_length=50)
    faculty_persian = models.CharField(max_length=100)
    
    
#choice for table Book
YEAR_CHOICES = []
for r in range(1980, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r,r))

class Book(models.Model):
    signtory = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    ISBN =  models.CharField(max_length=30)
    pages = models.IntegerField()
    langauge_id = models.ForeignKey(Langauge, on_delete=models.CASCADE)
    edition = models.IntegerField()
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher_id = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publiction_year = models.IntegerField(_('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    section_id = models.ForeignKey(Section, on_delete=models.CASCADE)
    faculty_id = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    description = models.TextField()
    
    
class Copy(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    status =  models.CharField(max_length=20)
    
    
class Ebook(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    extension =  models.CharField(max_length=30)
    
    
class New(models.Model):
    news_title = models.CharField(max_length=100)
    news_summary = models.TextField()
    news_dtails = models.TextField()
    news_ref = models.CharField(max_length=255)
    bews_title_persain = models.CharField(max_length=100)
    news_summary_persian = models.TextField()
    news_dtails_persain = models.TextField()
    news_ref_persain = models.CharField(max_length=255)
    news_date = models.DateField()
    fileext = models.CharField(max_length=3)
    faculty_id = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    

class Library(models.Model):
    faculty_id = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    content = models.TextField()
    content_persian = models.TextField()
    privacy = models.TextField()
    privacy_persian = models.TextField()
    services = models.TextField()
    services_persain = models.TextField()
    email = models.EmailField()


    
    




