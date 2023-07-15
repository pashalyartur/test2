from django.urls import path
from . import views

urlpatterns = [
    path('', views.test_list, name='test_list'),
    path('test/<int:test_id>/', views.test_detail, name='test_detail'),
    path('test/<int:test_id>/submit/', views.submit_test, name='submit_test'),
    path('result/<int:result_id>/', views.test_result, name='test_result'),
    path('teacher/', views.teacher, name='teacher'),
    path('teacher/<int:test_id>/results/', views.infa, name='infa'),
    path('tests/<int:test_id>/results/html/', views.generate_test_results_html, name='generate_test_results_html'),
]
