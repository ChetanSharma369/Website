from home.views import index, person, person_delete, login_view, Persondetail, PersonDetailViewSet
from django.urls import path, include

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', PersonDetailViewSet, basename='users')
urlpatterns = router.urls

urlpatterns=[
    path('index/', index, name='index'),
    path('person/', person, name='person'),
    path('person/<int:id>/delete/',person_delete, name='person_delete'),
    path('login/', login_view, name='login'),
    path('personview/', Persondetail.as_view(), name='person_detail'),
    path('',include(router.urls))
]