# Generated by Django 3.2.5 on 2021-07-26 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0020_auctionitem_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='WatchList',
            field=models.ManyToManyField(blank=True, related_name='users', to='auctions.AuctionItem'),
        ),
    ]
