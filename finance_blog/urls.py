from django.urls import path
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required

from .views import say_hello, BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView


urlpatterns = [
    path('hello/', say_hello),
    path('', TemplateView.as_view(template_name='start_page.html'), name='start'),
    path('home/', login_required(BlogListView.as_view()), name='home'),
    # path('home/', BlogListView.as_view(), name='home'),
    path('post/<int:pk>/', login_required(BlogDetailView.as_view()), name='post_detail'),
    path('post/create/', login_required(BlogCreateView.as_view()), name='post_create'),
    path('post/update/<int:pk>/', login_required(BlogUpdateView.as_view()), name='post_update'),
    path('post/delete/<int:pk>/', login_required(BlogDeleteView.as_view()), name='post_delete'),
]
