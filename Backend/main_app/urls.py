
from django.contrib import admin
from django.urls import path , include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    
    path("/", views.portfolio_view, name='dashboard'),
    path("admin-upload/", views.admin_upload_view, name='UploadNow'),
    path("Contact-us/", views.contact_us, name='ContactUs'),
    path("Skills/", views.skills_view, name='skills'),
    path("Certificates/", views.certificates_view, name='certificate'),
    path('blog/<int:blog_id>/', views.project_view, name='project'),
    path("UIUX/", views.uiux_view, name='uiux'),
    path("Unityprojects/", views.unity_view, name='unity'),
    path("appWebDev/", views.app_view, name='appWeb'),
    path("Projects/", views.projects_view, name='projects'),
    
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
