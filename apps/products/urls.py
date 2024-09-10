from django.urls import path
import apps.products.views as views

urlpatterns = [
    path('add_review/',views.AddReviewView.as_view(),name='add_review'),
    path('review/',views.ReviewListView.as_view(),name='review'),
    path('shoes/',views.ShoeDetailView.as_view(),name='shoe'),
]