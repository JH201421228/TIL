# Generated by Django 4.2.2 on 2023-10-19 03:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='articel',
            new_name='article',
        ),
    ]
