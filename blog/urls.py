from django.urls import path,include
import blog.views

# url指向方法，类比springboot controller层

urlpatterns = [
    path('hello_world', blog.views.hello_world),
    path('content', blog.views.article_content),
    path('index', blog.views.get_index_page),
    path('detail/<int:article_id>', blog.views.get_detial_page)
    #path('detail', blog.views.get_detial_page)
]