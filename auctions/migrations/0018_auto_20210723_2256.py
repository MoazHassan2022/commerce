# Generated by Django 3.2.5 on 2021-07-23 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0017_auto_20210723_1921'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auctionitem',
            old_name='description',
            new_name='Description',
        ),
        migrations.RemoveField(
            model_name='auctionitem',
            name='Price',
        ),
    ]
