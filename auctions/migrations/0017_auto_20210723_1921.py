# Generated by Django 3.2.5 on 2021-07-23 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0016_auto_20210723_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionitem',
            name='Category',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='auctionitem',
            name='ImageURL',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
    ]