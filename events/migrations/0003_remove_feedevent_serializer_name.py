# Generated by Django 4.2.6 on 2023-10-23 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedevent',
            name='serializer_name',
        ),
    ]