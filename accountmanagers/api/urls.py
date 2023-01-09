from django.urls import path, include
from accountmanagers.api import views



urlpatterns = [
    path('partner/',views.PartnerViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('partner/<int:pk>/', views.PartnerViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'confirmPartner'})),
    
]