from __future__ import unicode_literals
import os
from django.contrib.auth.models import User
from django.db import models

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

class UserCategories(models.Model):
    """Per user categoy list
    """
    name = models.CharField(max_length=256)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.name

class Artwork(models.Model):
    """Individual piece of art
    """
    name = models.CharField(max_length=256)
    inventory_id = models.CharField(max_length=32)
    media = models.ManyToManyField(UserMedia)
    finished = models.BooleanField(default=True)
    user = models.ForeignKey(User)
    categories = models.ManyToManyField(UserCategories)

    # Dimensions
    #http://stackoverflow.com/questions/413446/django-and-units-conversion
    height = models.CharField(max_length=20)
    #height_units = models.CharField(max_length=5, choices=UNITS_LENGTH)
    width = models.CharField(max_length=20)
    #width_units = models.CharField(max_length=2, choices=UNITS_LENGTH)
    depth = models.CharField(max_length=20)
    #depth_units = models.CharField(max_length=2, choices=UNITS_LENGTH)
    # Other Dims
    mass = models.CharField(max_length=20)
    #mass_units = models.CharField(max_length=2, choices=UNITS_MASS)

    shared = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def usersMedia(self):
        artwork_media = self.media.all()
        for m in UserMedia.objects.filter(user=self.user).all():
            if m in artwork_media:
                m.isApplied = True
            yield m


class ArtworkView(models.Model):
    image = models.ImageField(blank=True, null=True)
    artwork = models.ForeignKey(Artwork)

    def getMasonryCss(self):
        # Return css class, size
        iw = self.image.width

        w_css = {
            160: 'grid-item--width1',
            320: 'grid-item--width2',
            480: 'grid-item--width3',
            640: 'grid-item--width4',
        }

        # .grid-item--width2 { width: 320px; }
        # .grid-item--width3 { width: 480px; }
        # .grid-item--width4 { width: 640px; }
        nearestWidth = min(w_css.keys(), key=lambda x:abs(x - iw))

        return w_css.get(nearestWidth)
