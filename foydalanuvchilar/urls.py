from django.urls import path
from .views import user_view

urlpatterns = [
    path('users/', user_view, name = 'users_page'),
    path('<int:id>', user_view, name='id_page')
]
