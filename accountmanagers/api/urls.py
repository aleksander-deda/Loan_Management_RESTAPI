from django.urls import path, include
from accountmanagers.api import views



urlpatterns = [
    path('partner/',views.PartnerViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('partner/<int:pk>/', views.PartnerViewSet.as_view({'get': 'retrieve', 'put': 'update'})),
    path('partner-confirmation/<int:pk>/', views.PartnerViewSet.as_view({'patch': 'confirmPartner', 'put': 'confirmModifiedPartner'})),
    
    path('super-partner/',views.SuperPartnerViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('super-partner/<int:pk>/', views.SuperPartnerViewSet.as_view({'get': 'retrieve', 'put': 'update'})),
    path('super-partner-confirmation/<int:pk>/', views.SuperPartnerViewSet.as_view({'patch': 'confirmSuperPartner', 'put': 'confirmModifiedSuperPartner'})),
    
]