from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from coverage_tracker import views

urlpatterns = [
    path('all/', views.staffer_list),
    path('by_comp_id/<str:comp_id>/', views.staffer_by_comp_id),
    path('by_dorm/<str:dorm>/', views.staffer_by_dorm)
]

urlpatterns = format_suffix_patterns(urlpatterns)