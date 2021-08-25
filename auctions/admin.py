from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(AuctionItem)
admin.site.register(User)
admin.site.register(Comment)
admin.site.register(bid)
admin.site.register(closedAuctionItem)