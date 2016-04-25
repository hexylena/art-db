# encoding: utf-8
from django.core.management.base import BaseCommand, CommandError
from web.models import Artwork, UserMedia, ArtworkView
from django.contrib.auth.models import User
from faker import Faker
fake = Faker()
import glob
import os
import shutil
import random

media_tags = [
    u'Airbrush',
    u'Acrylic paint',
    u'Chalk',
    u'Charcoal',
    u'Coloured pencil',
    u'Conté',
    u'Crayon',
    u'Gouache',
    u'Graphite',
    u'Human finger',
    u'Marker',
    u'Oil paint',
    u'Pastel',
    u'Pen and ink',
    u'Pencil',
    u'Sand',
    u'Tempera',
    u'Watercolor',
]

class Command(BaseCommand):
    help = 'Generate fake data'

    def add_arguments(self, parser):
        parser.add_argument('image_dir', nargs='+')

    def handle(self, *args, **options):
        image_list = []

        for d in options['image_dir']:
            image_list += glob.glob(d + '/*.jpg')
            image_list += glob.glob(d + '/*.png')
            image_list += glob.glob(d + '/*.gif')

        for i in range(2):
            fp = fake.simple_profile()
            user = User.objects.create_user(
                username=fp['username'],
                email=fp['mail'],
                password='password',
            )
            print user.username

            usermedia = random.sample(media_tags, 6)
            um = []
            for x in usermedia:
                umm = UserMedia(name=x, user=user)
                umm.save()
                um.append(umm)

            for j in range(20):
                a = Artwork(
                    name=fake.pystr(max_chars=20),
                    inventory_id=str(fake.pyint()),
                    finished=fake.pybool(),
                    user=user,
                    height=fake.pyint(),
                    width=fake.pyint(),
                    depth=fake.pyint(),
                    mass=fake.pyint(),
                    shared=fake.pybool(),
                )
                a.save()
                q = random.sample(um, random.choice((1, 2, 3)))
                a.media = q
                a.save()

                for j in range(random.choice(range(1, 4))):
                    img = random.choice(image_list)
                    shutil.copy(img, 'media')
                    outimg = os.path.basename(img)
                    av = ArtworkView(
                        image=outimg,
                        artwork=a
                    )

                    av.save()
