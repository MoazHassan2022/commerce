# Generated by Django 3.2.5 on 2021-07-26 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0019_auctionitem_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionitem',
            name='username',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
    ]