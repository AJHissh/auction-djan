# Generated by Django 4.0.1 on 2023-01-05 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_alter_listings_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='listings',
            name='file',
            field=models.FileField(default='None', upload_to='images/'),
        ),
    ]