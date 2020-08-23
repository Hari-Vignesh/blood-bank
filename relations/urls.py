from django.urls import path
from . import views

app_name = 'relations'

urlpatterns = [
    path('', views.people_list, name='home'),
    path('new', views.add_person, name='add_person'),
    path('<int:pk>', views.people_detail, name='detail'),
    path('<int:pk>/receives', views.people_receives, name='receives'),
    path('<int:pk>/gives', views.people_gives, name='gives'),
]
