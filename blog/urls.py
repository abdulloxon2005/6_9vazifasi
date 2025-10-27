from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path('maqola/<int:pk>', views.maqola, name='maqola')
]