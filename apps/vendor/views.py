from django.views.generic import ListView, DetailView, CreateView
from apps.vendor.models import Vendor, VendorReview
from apps.products.models import Shoe
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

class VendorListView(ListView):
    model = Vendor
    template_name = 'vendors/vendor_list.html'
    context_object_name = 'vendors'

class VendorDetailView(DetailView):
    model = Vendor
    template_name = 'vendors/vendor_detail.html'
    context_object_name = 'vendor'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shoes'] = Shoe.objects.filter(vendor=self.object)
        context['reviews'] = VendorReview.objects.filter(vendor=self.object)
        return context

class VendorShoeListView(ListView):
    model = Shoe
    template_name = 'vendors/vendor_shoe_list.html'
    context_object_name = 'shoes'

    def get_queryset(self):
        self.vendor = get_object_or_404(Vendor, pk=self.kwargs['vendor_id'])
        return Shoe.objects.filter(vendor=self.vendor)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vendor'] = self.vendor
        return context

class VendorReviewListView(ListView):
    model = VendorReview
    template_name = 'vendors/vendor_review_list.html'
    context_object_name = 'reviews'

    def get_queryset(self):
        self.vendor = get_object_or_404(Vendor, pk=self.kwargs['vendor_id'])
        return VendorReview.objects.filter(vendor=self.vendor)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vendor'] = self.vendor
        return context

class AddVendorReviewView(LoginRequiredMixin, CreateView):
    model = VendorReview
    template_name = 'vendors/add_vendor_review.html'
    fields = ['rating', 'comment']
    success_url = reverse_lazy('vendors:vendor_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.vendor = get_object_or_404(Vendor, pk=self.kwargs['vendor_id'])
        return super().form_valid(form)
