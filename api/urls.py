from home.views import index, person, person_delete
from django.urls import path 

urlpatterns=[
    path('index/', index, name='index'),
    path('person/', person, name='person'),
    path('person/<int:id>/delete/',person_delete, name='person_delete'),
]