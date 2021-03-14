from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from users import views

urlpatterns = [
    path('', views.UserViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('me/', views.MeView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)