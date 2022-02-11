from django.db import migrations
import json


def create_data(apps, schema_editor):
    Movie = apps.get_model('films', 'Movie')
    dest_src = '/Users/artemut/WebstormProjects/movies/src/data/movie500.json'
    with open(dest_src) as json_file:
        json_data = json.load(json_file)

    for movie in json_data:
        Movie(**movie).save()



class Migration(migrations.Migration):
    dependencies = [
        ('films', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(create_data),
    ]
