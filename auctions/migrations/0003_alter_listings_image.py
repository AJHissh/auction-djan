# Generated by Django 4.0.1 on 2022-12-16 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_listings_image_alter_bids_bid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='image',
            field=models.ImageField(blank=True, default='None', upload_to='users/%Y/%m/%d/'),
        ),
    ]
