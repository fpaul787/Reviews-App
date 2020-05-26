from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Review
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from comments.forms import CommentForm
from django.views.generic.edit import FormMixin

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
    paginate_by = 5

class UserReviewsListView(ListView):
    model = Review
    template_name = 'user_reviews.html'
    context_object_name = 'reviews'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Review.objects.filter(author=user).order_by('-date_posted')


class ReviewDetailView(FormMixin,DetailView):
    model = Review   
    template_name = 'review_detail.html'
    form_class = CommentForm
    
    def get_context_data(self, **kwargs):
        context = super(ReviewDetailView, self).get_context_data(**kwargs)
        
        # context['form'] = CommentForm(initial={
        #     'review': self.object
        # })
        # getting all the comments for this review
        context['comments'] = self.object.comment_set.filter(review=context['object'])
        #print(context['comments'].values())
        print(context['form'])
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        print(form)
        #print(request.POST.get("my_textarea"))
        return HttpResponse(None)

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        
        form.save()
        return super(ReviewDetailView, self).form_valid(form)
    
    # def form_valid(self, form):
    #     print('Worked')
    #     return HttpResponse(None)

    # def post(self, request, *args, **kwargs):
    #     #print(self.request.user) author check
    #     # print(kwargs['pk']) review ID check
    #     #print(Review.objects.get(pk=kwargs['pk'])) review check
        
    #     return HttpResponse(None)

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
        return super().form_valid(form)

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
