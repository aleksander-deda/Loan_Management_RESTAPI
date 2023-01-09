from django.urls import path, include
from superadmin.api import views

urlpatterns = [
    
    path('account-manager/', views.AccountManagerViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('account-manager/<int:pk>/', views.AccountManagerViewSet.as_view({'get': 'retrieve', 'put': 'update'})),

    path('underwriter/', views.UnderwriterViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('underwriter/<int:pk>/', views.UnderwriterViewSet.as_view({'get': 'retrieve', 'put': 'update'})),
    
    path('product/', views.ProductViewSet.as_view({'get': 'list', 'post': 'create'})), 
    path('product/<int:pk>/', views.ProductViewSet.as_view({'get': 'retrieve', 'put': 'update'})),
    
    path('loan-config/', views.LoanConfigViewSet.as_view({'get': 'list', 'post': 'create'})), 
    path('loan-config/<int:pk>/', views.LoanConfigViewSet.as_view({'get': 'retrieve', 'put': 'update'})),
    
    path('bank/', views.BankViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('bank/<int:pk>/', views.BankViewSet.as_view({'get': 'retrieve', 'put': 'update'})),
    
    path('city/', views.CityViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('city/<int:pk>/', views.CityViewSet.as_view({'get': 'retrieve', 'put': 'update'})),
    
    path('membertype/', views.MemberTypeViewSet.as_view({'get': 'list', 'post': 'create'})), 
    path('membertype/<int:pk>/', views.MemberTypeViewSet.as_view({'get': 'retrieve', 'put': 'update'})),
    
    
]