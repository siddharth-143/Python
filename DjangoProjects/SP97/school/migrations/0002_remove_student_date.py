# Generated by Django 3.2.8 on 2021-11-28 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='date',
        ),
    ]
