from django.db import models

# Create your models here.

# one-to-many relation, one location can have many users 
class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.name} ({self.address})"

class Participant(models.Model):
    email = models.EmailField(unique=True)  # can't store multiple same address

    def __str__(self):
        return self.email


class Meetup(models.Model):
    title = models.CharField(max_length=200)
    organizer_email = models.EmailField()
    date = models.DateField()
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    participants = models.ManyToManyField(Participant, blank=True, null=True)

    # a default constructor to display the name in admin 
    def __str__(self):
        return f'{self.title} - {self.slug}'