from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=200)
    date_of_birth = models.DateField('date of birth', null=True, blank=True)
    date_of_death = models.DateField('date of death', null=True, blank=True)

    def __str__(self):
        return "{} ({})".format(self.name, self.date_of_birth)

class Genre(models.Model):
    # NAMES = (
    #     ('SF', 'Science fiction'),
    #     ('S', 'Satire'),
    #     ('AA', 'Action and Adventure'),
    #     ('R', 'Romance'),
    #     ('M', 'Mystery'),
    #     ('H', 'Horror'),
    #     ('SH', 'Self help'),
    #     ('H', 'Health'),
    #     ('G', 'Guide'),
    #     ('HI', 'History'),
    #     ('SC', 'Science'),
    #     ('CO', 'Cookbooks'),
    # )
    # name = models.CharField(max_length=2, choices=NAMES)
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField('date published', null=True,  blank=True)
    synopsis = models.TextField(max_length=2500,blank=True)
    path_to_img = models.CharField(max_length=260)
    photo = models.ImageField(upload_to='books', null=True)


    # need to add the price of the book here !
    buy_price = models.FloatField(blank=True, null=True)
    rent_price = models.FloatField(blank=True, null=True)

    authors = models.ManyToManyField(Author, verbose_name="Author")
    genres  = models.ManyToManyField(Genre, verbose_name="Genre")

    def __str__(self):
        return self.title

#class Book_Author(models.Model):
    
    #book = models.ForeignKey(Book, null=True, on_delete=models.CASCADE)
    #author = models.ForeignKey(Author, null=True, on_delete=models.CASCADE)

# class Book_Genre(models.Model):
#     book = models.ForeignKey(Book, on_delete=models.CASCADE)
#     genre =  models.ForeignKey(Genre, on_delete=models.CASCADE)