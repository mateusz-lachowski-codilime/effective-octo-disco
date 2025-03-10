from django.urls import path
from .views import (
    NetworkDeviceList, NetworkDeviceDetail, InterfaceList, InterfaceDetail,
    SubnetList, SubnetDetail, LinkList, LinkDetail, DeviceGroupList, DeviceGroupDetail,
    VLANList, VLANDetail, DeviceEventList, DeviceEventDetail, RoutingTableList, RoutingTableDetail
)

urlpatterns = [
    path('network-devices/', NetworkDeviceList.as_view()),
    path('network-devices/<int:pk>/', NetworkDeviceDetail.as_view()),

    path('interfaces/', InterfaceList.as_view()),
    path('interfaces/<int:pk>/', InterfaceDetail.as_view()),

    path('subnets/', SubnetList.as_view()),
    path('subnets/<int:pk>/', SubnetDetail.as_view()),

    path('links/', LinkList.as_view()),
    path('links/<int:pk>/', LinkDetail.as_view()),

    path('device-groups/', DeviceGroupList.as_view()),
    path('device-groups/<int:pk>/', DeviceGroupDetail.as_view()),

    path('vlans/', VLANList.as_view()),
    path('vlans/<int:pk>/', VLANDetail.as_view()),

    path('device-events/', DeviceEventList.as_view()),
    path('device-events/<int:pk>/', DeviceEventDetail.as_view()),

    path('routing-tables/', RoutingTableList.as_view()),
    path('routing-tables/<int:pk>/', RoutingTableDetail.as_view()),
]