from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("listings/<int:ID>", views.listing, name="listing"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("add/<int:LID>", views.addToWatchlist, name="addToWatchlist"),
    path("remove/<int:LID>", views.removeWatchlist, name="removeWatchlist"),
    path("categories", views.categories, name="categories"),
    path("category/<str:cat>", views.category, name="category"),
    path("close/<int:ID>", views.closeListing, name="close"),
    path("closedListing/<int:ID>", views.closedListing, name="closedListing"),
    path("comment/<int:ID>", views.addComent, name="comment"),
]
