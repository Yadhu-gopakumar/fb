from django.urls import path
from . import views
app_name='home'
urlpatterns = [
    path('', views.home,name='home'),
    path('profile/<str:user>/',views.profile,name='profile'),
    path('like/<int:id>/',views.like,name='like'),
    path('comment/<int:id>/',views.comment,name='comment'),
    path('deletecomment/<int:id>/',views.deletecomment,name='deletecomment'),
    path('profile/<str:user>/follow/',views.follow,name='follow'),
    path('addpost/',views.addpost,name='addpost'),
    path('edit/',views.edit,name='edit'),
    path('search/',views.search,name='search'),
]
