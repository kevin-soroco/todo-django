from django.urls import path

from kartecom import views

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('index/', views.index, name='index'),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("todo/", views.todo_create.as_view(), name="todo_create"),
]
