from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ai-advantage/', views.ai_advantage, name='ai_advantage'),
    path('skill-test/', views.skill_test, name='skill_test'),
    path('learning-system/', views.learning_system, name='learning_system'),
    path('career-roadmap/', views.career_roadmap, name='career_roadmap'),
    path('career-capsules/', views.career_capsules, name='career_capsules'),
    path('language-barrier/', views.language_barrier, name='language_barrier'),
]
