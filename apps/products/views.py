from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from apps.products.models import Category, Shoe, Review
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class ShoeCreateView(CreateView):
    model = Shoe
    template_name = 'shoe/create.html'
    fields = ['name', 'price', 'description', 'category', 'image']
    success_url = reverse_lazy('products:shoe_list')
    

class ShoeListView(ListView):
    model = Shoe
    template_name = 'products/shoe_list.html'
    context_object_name = 'shoes'

# ShoeDetailView - Displays details of a specific shoe
class ShoeDetailView(DetailView):
    model = Shoe
    template_name = 'products/shoe_detail.html'
    context_object_name = 'shoe'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shoes'] = Shoe.objects.filter(category=self.object)
        return context

# ReviewListView - Lists reviews for a shoe
class ReviewListView(ListView):
    model = Review
    template_name = 'products/review_list.html'
    context_object_name = 'reviews'

    def get_queryset(self):
        shoe = get_object_or_404(Shoe, pk=self.kwargs['shoe_id'])
        return Review.objects.filter(shoe=shoe)

# AddReviewView - Form to submit a review
class AddReviewView(LoginRequiredMixin, CreateView):
    model = Review
    template_name = 'products/add_review.html'
    fields = ['rating', 'comment']
    success_url = reverse_lazy('products:shoe')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.shoe = get_object_or_404(Shoe, pk=self.kwargs['shoe_id'])
        return super().form_valid(form)
