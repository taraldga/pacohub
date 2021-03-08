from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from pacount import views

urlpatterns = [
    path('fields/', views.FieldList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)