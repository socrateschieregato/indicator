from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from balance.views import ChargeViewSet, EquipmentViewSet
from ports.views import PortsAPIView

urlpatterns = [
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    path('ports/', PortsAPIView.as_view(), name='get_port_api'),
    path('weight/', ChargeViewSet.as_view({'get': 'retrieve', 'post': 'create'}), name='get_charge_api'),
    path('charges/', ChargeViewSet.as_view({'get': 'list'}), name='get_charges_api'),
    path('equipments/', EquipmentViewSet.as_view({'get': 'list'}), name='get_equipment_api'),
]
