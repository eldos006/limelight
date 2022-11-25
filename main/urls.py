from django.urls import path
from api.views import CarAPIViews, NewsApiView
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('<int:id>', views.home_home, name='home'),
    path('index/', views.index, name='index'),
    path('form/', views.form, name='form'),
    path('news/', views.news, name='news'),
    path('news_form/', views.news_form, name='news_form'),
    path('more/<int:id>', views.more, name='more'),
    path('more-news/', views.more_news, name='more-news'),
    path('profile/<int:id>', views.profile, name='profile'),
    path('delete/<int:pk>', views.del_view, name='delete'),
    path('all/', CarAPIViews.as_view(), name='all'),
    path('api/', NewsApiView.as_view(), name='api'),
]
