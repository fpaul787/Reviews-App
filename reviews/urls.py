from django.urls import path
from .views import (
    ReviewListView, 
    ReviewDetailView, 
    ReviewCreateView, 
    ReviewUpdateView, 
    ReviewDeleteView,
    UserReviewsListView)
from . import views

urlpatterns = [
    # path('', views.home, name="reviews-home"),
    # path('home', ReviewListView.as_view(), name='reviews-home'),
    path('home', views.reviews_list, name='reviews-home'),
    path('user/<str:username>', UserReviewsListView.as_view(), name='user-reviews'),
    # path('review/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
    path('review/<slug:slug>/', ReviewDetailView.as_view(), name='review-detail'),
    path('review/<int:pk>/update', ReviewUpdateView.as_view(), name="review-update"),
    path('review/<int:pk>/delete', ReviewDeleteView.as_view(), name="review-delete"),
    path('review/create', ReviewCreateView.as_view(), name="review-create"),
    path('like/', views.review_like, name='review-like'),
    

]
