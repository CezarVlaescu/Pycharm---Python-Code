from django.urls import path

from App import views

app_name = 'blog'

urlpatterns = [
    path('', views.AdminArticleListView.as_view(), name='home'),
    path('article/<int:pk>', views.AdminArticleDetailView.as_view(), name='detail'),
    path('create_blog/', views.PostView.as_view(), name='create_blog')
]