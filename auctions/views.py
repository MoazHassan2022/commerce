from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import *
from datetime import datetime

Categories = ["Electronics", "Home", "Fashion", "Toys", "Cars", "Furniture"]

def index(request):
    aucs = AuctionItem.objects.all()
    closedAucs = closedAuctionItem.objects.all()
    return render(request, "auctions/index.html", {
       "aucs":aucs,
        "closedAucs":closedAucs
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def create(request):
    if request.method=="POST":
        Title = request.POST["Title"]
        Description = request.POST["Description"]
        StartingBid = request.POST["StartingBid"]
        ImageURL = request.POST["ImageURL"]
        Category = request.POST["Category"]
        date = datetime.now()
        username = request.user.username
        auc = AuctionItem(Title=Title, Description=Description, ImageURL=ImageURL, StartingBid=StartingBid, Category=Category, date=date, username=username)
        auc.save()
        return HttpResponseRedirect("/")
    return render(request, "auctions/create.html", {
        "Categories":Categories
    })

def listing(request, ID):
    exists = False
    auc = AuctionItem.objects.get(id=ID)
    commentList = auc.commentList.all()
    if request.user.is_authenticated:
        watch = request.user.WatchList.all()
        for w in watch:
            if auc.Title == w.Title:
                exists = True

    NotDone = False
    if request.method == "POST":
        Bid = request.POST["bid"]
        start = auc.StartingBid
        if int(Bid[1:]) >= int(start[1:]):
            List = auc.bidList.all()
            larger = True
            for b in List:
                price = b.Price
                if int(price[1:]) >= int(Bid[1:]):
                    larger = False
            if larger:
                bidObject = bid(Price=Bid, Creator=request.user.username)
                bidObject.save()
                auc.bidList.add(bidObject)
            else:
                NotDone=True
        else:
            NotDone=True
        ListAfter = auc.bidList.all()
        bidCount = 0
        for b in ListAfter:
            bidCount = bidCount + 1
        message =""
        if NotDone:
            message = "Please make a bid larger than the starting bid or the other bids"
        return render(request, "auctions/Listing page.html", {
            "auc": auc,
            "exists": exists,
            "count":bidCount,
            "message":message,
            "commentList":commentList
        })

    else:
        List = auc.bidList.all()
        bidCount = 0
        for b in List:
            bidCount = bidCount + 1
        return render(request, "auctions/Listing page.html", {
            "auc":auc,
            "exists":exists,
            "count": bidCount,
            "commentList":commentList
        })

def watchlist(request):
    watch = request.user.WatchList.all()
    return render(request, "auctions/watchlist.html", {
        "watchlist":watch
    })

def addToWatchlist(request, LID):
    Listing = AuctionItem.objects.get(id=LID)
    request.user.WatchList.add(Listing)
    return HttpResponseRedirect(f"../listings/{LID}")

def removeWatchlist(request, LID):
    auc = AuctionItem.objects.get(id=LID)
    request.user.WatchList.remove(auc)
    return HttpResponseRedirect(f"../listings/{LID}")

def categories(request):
    return render(request, "auctions/Categories.html",{
        "categories":Categories
    })

def category(request, cat):
    List = AuctionItem.objects.filter(Category=cat)
    return render(request, "auctions/category.html",{
        "category":cat,
        "List":List
    })

def closeListing(request, ID):
    Listing = AuctionItem.objects.get(id=ID)
    BidL = Listing.bidList.all()
    LargestBid = BidL[0]
    for b in BidL:
        if b.Price > LargestBid.Price:
            LargestBid = b

    closed = closedAuctionItem(Title=Listing.Title, Description=Listing.Description, ImageURL=Listing.ImageURL, StartingBid = Listing.StartingBid, Category = Listing.Category, date = Listing.date, username = Listing.username, WinnerUsername = LargestBid.Creator)
    closed.save()
    closed.commentList.set(Listing.commentList.all())
    Listing.delete()

    return HttpResponseRedirect("/")

def closedListing(request, ID):
    auc = closedAuctionItem.objects.get(id=ID)
    commentList = auc.commentList.all()
    return render(request, "auctions/Closed listing page.html", {
        "auc":auc,
        "commentList":commentList
    })

def addComent(request, ID):
    if request.method == "POST":
        auc = AuctionItem.objects.get(id=ID)
        CommentText = request.POST["comment"]
        username = request.user.username
        commentObject = Comment(CommentText=CommentText, username=username)
        commentObject.save()
        auc.commentList.add(commentObject)
        return HttpResponseRedirect(f"../listings/{ID}")