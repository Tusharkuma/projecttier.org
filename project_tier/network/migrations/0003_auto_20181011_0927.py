# Generated by Django 2.0.8 on 2018-10-11 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0002_auto_20180921_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='slug',
            field=models.SlugField(help_text='All lowercase, hyphenated name that will appear in the URL. For example, entering norm-medeiros will result in the URL projecttier.org/person/norm-medeiros'),
        ),
    ]
