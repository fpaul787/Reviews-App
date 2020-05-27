from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Review
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from comments.forms import CommentForm
from comments.models import Comment
from django.views.generic.edit import FormMixin
from django.http import HttpResponseRedirect


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
    success_url = ''
    
    def get_context_data(self, *args, **kwargs):
        context = super(ReviewDetailView, self).get_context_data(**kwargs)
        #print(self.kwargs['pk'])
        instance = get_object_or_404(Review, id=self.kwargs['pk'])
        #print(instance)

        # context['form'] = CommentForm(initial={
        #     'review': self.object
        # })
        # getting all the comments for this review

        content_type = ContentType.objects.get_for_model(Review)
        obj_id = instance.id

        context['content_type'] = content_type
        context['object_id'] = obj_id
        context['comments'] = Comment.objects.filter(content_type=content_type, object_id=obj_id)
        return context
    
    def post(self, request, *args, **kwargs):

        content_type = ContentType.objects.get_for_model(Review)
        instance_id = kwargs['pk']        
        
        if len(request.POST.get("my_textarea")) > 0:            
            comment = Comment(author=request.user, content_type=content_type, object_id=instance_id,content= request.POST.get("my_textarea"))
            comment.save()
            return HttpResponseRedirect(self.request.path_info)
        else:
            # not valid request
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
