# terminal/urls.py

from django.urls import path

urlpatterns = [
    path('dashboard/', lambda request: None, name='ec2_dashboard'),  # 임시로 대체
    path('start/<str:instance_id>/', lambda request, instance_id: None, name='start_instance'),
    path('stop/<str:instance_id>/', lambda request, instance_id: None, name='stop_instance'),
]

from . import views

urlpatterns = [
    path('dashboard/', views.ec2_dashboard, name='ec2_dashboard'),
    path('start/<str:instance_id>/', views.start_instance_view, name='start_instance'),
    path('stop/<str:instance_id>/', views.stop_instance_view, name='stop_instance'),
]
