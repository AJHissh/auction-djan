# Generated by Django 4.0.1 on 2023-01-04 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_alter_listings_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
