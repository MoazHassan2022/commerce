# Generated by Django 3.2.5 on 2021-07-23 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_auto_20210723_1833'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auctionitem',
            name='Image',
        ),
    ]
