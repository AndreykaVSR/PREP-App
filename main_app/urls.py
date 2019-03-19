from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home' ),
    path('about/', views.about, name='about' ),
    path('projects/', views.Index.as_view(), name='index' ),
    path('projects/<int:pk>/', views.Project_Detail.as_view(), name='detail' ),
    path('projects/new/', views.New_Project.as_view(), name='new_project' ),
    path('projects/<int:pk>/technology/', views.Add_Technology.as_view(), name='technology' ),
    path('projects/<int:pk>/image/', views.Add_Image.as_view(), name='image' ),
    path('projects/<int:project_id>/update/', views.Update_Project.as_view(), name='update_project' ),
    path('', views.add_new_teammate, name='add_new_teammate' ),
    path('reviews/<int:project_id/new/', views.new_review.as_view(), name='new_review' ),
    path('reviews/<int:project_id>/team_reviews/', views.consolidated_review, name='consolidated_review' ),
    path('user/', views.Profile, name='profile' ),
    path('user/new/', views.signup, name='register' ),
    path('', views.save_user, name='save_user' ),
]
