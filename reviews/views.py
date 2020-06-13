from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Review
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from comments.models import Comment
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.template.defaultfilters import slugify

from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
import json

# Create your views here.
posts = [
    {
        'author': 'Frantz',
        'title': 'The Miseducation of Lauryn Hill Review',
        'content': "First post content",
        'date_posted': "May 10, 2020"
    },
    {
        'author': 'Frantz',
        'title': 'Reasonable Doubt Review',
        'content': "First post content",
        'date_posted': "May 10, 2020"
    }
]

# function based view
def home(request):
    data = {
        'name': "Frantz"
    }

    context = {
        'data': data,
        'reviews': Review.objects.all()
    }
    return render(request, 'home.html' ,context)

class ReviewListView(ListView):
    model = Review
    template_name = 'home.html'
    context_object_name = 'reviews'
    ordering = ['-date_posted']
    paginate_by = 4

    def get_context_data(self, *args, **kwargs):
        context = super(ReviewListView, self).get_context_data(**kwargs)
        reviews = Review.objects.all()
        # print(reviews)
        context['reviews'] = reviews

        reviews = list(Review.objects.all().values())
        context['reviews_dictionary'] = json.dumps(reviews, cls=DjangoJSONEncoder)
        
        return context

class UserReviewsListView(ListView):
    model = Review
    template_name = 'user_reviews.html'
    context_object_name = 'reviews'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Review.objects.filter(author=user).order_by('-date_posted')

class ReviewDetailView(DetailView):
    model = Review   
    template_name = 'review_detail.html'
    
    success_url = ''
    
    def get_context_data(self, *args, **kwargs):
        # print(args)
        # print(self.kwargs)
        context = super(ReviewDetailView, self).get_context_data(**kwargs)
        
        instance = get_object_or_404(Review, slug=self.kwargs['slug'])
        
        content_type = ContentType.objects.get_for_model(Review)
        obj_id = instance.id

        context['content_type'] = content_type
        context['object_id'] = obj_id
        context['comments'] = Comment.objects.filter(content_type=content_type, object_id=obj_id)
        context['likes'] = instance.likes.all()
        return context
    
    def post(self, request, *args, **kwargs):
        content_type = ContentType.objects.get_for_model(Review)
        instance = Review.objects.get(slug=kwargs['slug'])       
        
        if request.POST.get('like'):
            if not request.user.is_anonymous:
                if instance.likes.filter(username=request.user):
                    instance.likes.remove(request.user)
                    return HttpResponseRedirect(self.request.path_info)
                else:
                    instance.likes.add(request.user)
                    return HttpResponseRedirect(self.request.path_info)
            else:
                messages.error(request, "You must be logged in to like", extra_tags="like")
                return HttpResponseRedirect(self.request.path_info)
        else:
            if not request.user.is_anonymous:
                if len(request.POST.get("comment_textarea")) > 0 and request.POST.get("comment_textarea") is not None:            
                    comment = Comment(author=request.user, content_type=content_type, 
                            object_id=instance.id,
                                content=request.POST.get("comment_textarea"))
                    comment.save()
                    

                    return HttpResponseRedirect(self.request.path_info)
                else:
                    # print('error')
                    messages.error(request, "You must type a comment", extra_tags="comment")
                    return HttpResponseRedirect(self.request.path_info)
            else:
                messages.error(request, "You must be logged in to comment", extra_tags="comment")
                return HttpResponseRedirect(self.request.path_info)

class ReviewCreateView(LoginRequiredMixin,CreateView):
    model = Review
    fields = ['title', 'content']
    template_name = 'review_form.html'

    success_url = reverse_lazy('reviews-home')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin ,UpdateView):
    model = Review
    fields = ['title', 'content']
    template_name = 'review_update.html'

    success_url = reverse_lazy('reviews-home')
    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super().form_valid(form)
        print(self.object.content)
        print(self.object.slug)
        self.object.slug = self.object.title
        print(self.object.slug)
        return response

    def test_func(self):
        review = self.get_object()
        if self.request.user == review.author:
            return True # allow update
        return False # can't update
    

class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    template_name = 'review_confirm_delete.html'
    success_url = '/'

    def test_func(self):
        review = self.get_object()
        if self.request.user == review.author:
            return True # allow deletion
        return False # can't delete
