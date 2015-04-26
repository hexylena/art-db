from django.db import models
from django.contrib.auth.models import User

UNITS_LENGTH = (
    ('m', 'meters'),
    ('cm', 'centimeters'),
    ('f', 'feet'),
    ('i', 'inches'),
)

UNITS_MASS = (
    ('kg', 'kilograms'),
    ('lb', 'pounds'),
)

class UserMedia(models.Model):
    """Per user media list
    """
    name = models.CharField(max_length=256)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.name

class Artwork(models.Model):
    """Individual piece of art
    """
    name = models.CharField(max_length=256)
    media = models.ManyToManyField(UserMedia)
    finished = models.BooleanField(default=True)
    user = models.ForeignKey(User)

    # Dimensions
    #http://stackoverflow.com/questions/413446/django-and-units-conversion
    height = models.FloatField()
    height_units = models.CharField(max_length=2, choices=UNITS_LENGTH)
    width = models.FloatField()
    width_units = models.CharField(max_length=2, choices=UNITS_LENGTH)
    depth = models.FloatField()
    depth_units = models.CharField(max_length=2, choices=UNITS_LENGTH)
    # Other Dims
    mass = models.FloatField()
    mass_units = models.CharField(max_length=2, choices=UNITS_MASS)

    def __str__(self):
        return self.name

class ArtworkView(models.Model):
    image = models.ImageField()
    artwork = models.ForeignKey(Artwork)
