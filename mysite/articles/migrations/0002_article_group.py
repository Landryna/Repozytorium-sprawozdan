# Generated by Django 2.1 on 2018-08-24 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='group',
            field=models.IntegerField(default=0),
        ),
    ]
