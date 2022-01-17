from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('accounts/signup/', views.signup, name='signup'),
  # Skills 
  path('skills/create/', views.SkillCreate.as_view(), name='skills_create'),
  path('skills/', views.skills_index, name='skills_index'),
  #Resume paths
  path('resumes/create/', views.ResumeCreate.as_view(), name='resumes_create'),
  path('resumes/<int:resume_id>/', views.resumes_detail, name='resumes_detail'),
  path('resumes/<int:resume_id>/assoc_skill/<int:skill_id>/', views.assoc_skill, name='assoc_skill'),

]