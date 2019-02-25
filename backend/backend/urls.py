
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from todo import views

router = routers.DefaultRouter()
router.register(r'todos', views.TodoView, 'todo')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]

"""
This is the final step that completes the building of the API,
 we can now perform CRUD operations 
 on the Todo model. The router class 
 allows us to make the following queries:

/todos/ - This returns a list of all the
 Todo items (Create and Read operations 
 can be done here).

/todos/id - this returns a single Todo 
item using the id primary key 
(Update and Delete operations can be done here).
"""
