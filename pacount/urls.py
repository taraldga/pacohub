from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from pacount import views

urlpatterns = [
    path('fields/', views.FieldList.as_view()),
    path('games/', views.GameListView.as_view()),
    path('game/', views.GameView.as_view()),
    path('game/<int:pk>/', views.GameView.as_view()),
    path('score/<int:pk>', views.ScoreView.as_view()),
    path('score/bulk/', views.BulkUpdateScoreView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)