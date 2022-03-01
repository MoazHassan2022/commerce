from django.contrib.auth.models import AbstractUser
from django.db import models


class bid(models.Model):
    Price = models.CharField(max_length=10, default="")
    Creator = models.CharField(max_length=64, default="")

class Comment(models.Model):
    CommentText = models.CharField(max_length=1000, default="")
    username = models.CharField(max_length=64, default="")

class AuctionItem(models.Model):
    Title = models.CharField(max_length=64, default="")
    Description = models.CharField(max_length=300, default="")
    ImageURL = models.CharField(max_length=1000, default="", blank=True)
    StartingBid = models.CharField(max_length=10, default="")
    Category = models.CharField(max_length=64, default="", blank=True)
    date = models.CharField(max_length=64, default="", blank=True)
    username = models.CharField(max_length=64, default="", blank=True)
    bidList = models.ManyToManyField(bid, blank=True, related_name="Items")
    commentList = models.ManyToManyField(Comment, blank=True, related_name="commentItems")
    def __str__(self):
        return f"{self.Title} : {self.Category}"

class closedAuctionItem(models.Model):
    Title = models.CharField(max_length=64, default="")
    Description = models.CharField(max_length=300, default="")
    ImageURL = models.CharField(max_length=1000, default="", blank=True)
    StartingBid = models.CharField(max_length=10, default="")
    Category = models.CharField(max_length=64, default="", blank=True)
    date = models.CharField(max_length=64, default="", blank=True)
    username = models.CharField(max_length=64, default="", blank=True)
    WinnerUsername = models.CharField(max_length=64, default="", blank=True)
    commentList = models.ManyToManyField(Comment, blank=True, related_name="closedCommentItems")
    def __str__(self):
        return f"{self.Title} : {self.Category}"

class User(AbstractUser):
    WatchList = models.ManyToManyField(AuctionItem, blank=True, related_name="users")
