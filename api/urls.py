from home.views import index, person, person_delete, login_view, Persondetail, StudentsViewSet, PeopleViewSet, RegisteringUser, LoginUser
from django.urls import path, include

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'students', StudentsViewSet, basename='students')
router.register(r'people', PeopleViewSet, basename='people')
urlpatterns = router.urls

urlpatterns=[
    path('index/', index, name='index'),
    path('person/', person, name='person'),
    path('person/<int:id>/delete/',person_delete, name='person_delete'),
    path('login/', login_view, name='login'),
    path('personview/', Persondetail.as_view(), name='person_detail'),
    path('',include(router.urls)),
    path('register/',RegisteringUser.as_view(), name='register'),
    path('loginuser/',LoginUser.as_view(), name='login')
]