# Generated by Django 4.0 on 2021-12-26 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_product_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, max_length=100, null=True, unique=True),
        ),
    ]
