from django.urls import path
from .views import ReviewListView, ReviewDetailView, ReviewCreateView, ReviewUpdateView
from . import views

urlpatterns = [
    # path('', views.home, name="reviews-home"),
    path('', ReviewListView.as_view(), name='reviews-home'),
    path('review/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
    path('review/<int:pk>/update', ReviewUpdateView.as_view(), name="review-update"),
    path('review/create', ReviewCreateView.as_view(), name="review-create")

]