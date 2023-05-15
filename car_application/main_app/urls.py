from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cars/', views.CarList.as_view(), name='car_list'),
    path('cars/<int:pk>/', views.car_detail, name='car_detail'),
    path('cars/create/', views.CarCreate.as_view(), name='car_create'),
    path('cars/<int:pk>/update/', views.CarUpdate.as_view(), name='car_update'),
    path('cars/<int:pk>/delete/', views.CarDelete.as_view(), name='car_delete'),
    path('cars/<int:car_id>/add_service', views.add_service, name='add_service'),
    path('upgrades/', views.UpgradeList.as_view(), name='upgrade_list'),
    path('upgrades/<int:pk>', views.UpgradeDetail.as_view(), name='upgrade_detail'),
    path('upgrades/create/', views.UpgradeCreate.as_view(), name='upgrade_create'),
    path('upgrades/<int:pk>/update', views.UpgradeUpdate.as_view(), name='upgrade_update'),
    path('upgrades/<int:pk>/delete', views.UpgradeDelete.as_view(), name='upgrade_delete'),
    path('cars/<int:car_id>/assoc_upgrade/<int:upgrade_id>', views.assoc_upgrade, name='assoc_upgrade'),
    path('cars/<int:car_id>/unassoc_upgrade/<int:upgrade_id>', views.unassoc_upgrade, name='unassoc_upgrade'),
    path('accounts/signup/', views.signup, name='signup'),
]