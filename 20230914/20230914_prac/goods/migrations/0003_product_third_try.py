# Generated by Django 4.2.5 on 2023-09-14 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_product_created_at_product_how_about_this_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='third_try',
            field=models.BooleanField(default=True),
        ),
    ]
