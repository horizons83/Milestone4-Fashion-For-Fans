from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('<int:blogpost_id>/',
         views.blog_detail,
         name='blog_detail'
         ),
    path('add/',
         views.add_blogpost,
         name='add_blogpost'
         ),
    path('comment/<int:blogpost_id>/',
         views.blog_comment,
         name='blog_comment'
         ),
    path('delete_comment/<int:comment_id>/',
         views.delete_comment,
         name='delete_comment'
         ),
]
