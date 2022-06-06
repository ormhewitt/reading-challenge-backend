from django.urls import path
from . import views

app_name = 'challenges'

urlpatterns = [
    path('', views.IndexView.as_view(), name=''),
    path('<int:pk>/', views.ChallengeView.as_view(), name= 'challenge'),
    path('add-challenge/', views.AddChallengeView.as_view(),name='newChallenge'),
    # path('update-challenge/', views.UpdateChallengeView.as_view(), name='updateChallenge')
]