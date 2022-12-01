from django.urls import path
from Myapp import views

urlpatterns = [
    path('', views.Cv_BuildView, name='resume_view'),
    path('user/<int:id>/', views.Resume, name='user_resume'),
    path('resume_pdf/<int:id>', views.Resume_pdf, name='resume-pdf'),
]
