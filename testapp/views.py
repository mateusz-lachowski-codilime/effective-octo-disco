from django.shortcuts import render

from rest_framework import generics
from .models import (
    NetworkDevice, Interface, Subnet, Link, DeviceGroup, VLAN, DeviceEvent, RoutingTable
)
from .serializers import (
    NetworkDeviceSerializer, InterfaceSerializer, SubnetSerializer, LinkSerializer,
    DeviceGroupSerializer, VLANSerializer, DeviceEventSerializer, RoutingTableSerializer
)

class NetworkDeviceList(generics.ListCreateAPIView):
    queryset = NetworkDevice.objects.all()
    serializer_class = NetworkDeviceSerializer

class NetworkDeviceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = NetworkDevice.objects.all()
    serializer_class = NetworkDeviceSerializer

class InterfaceList(generics.ListCreateAPIView):
    queryset = Interface.objects.all()
    serializer_class = InterfaceSerializer

class InterfaceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Interface.objects.all()
    serializer_class = InterfaceSerializer

class SubnetList(generics.ListCreateAPIView):
    queryset = Subnet.objects.all()
    serializer_class = SubnetSerializer

class SubnetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subnet.objects.all()
    serializer_class = SubnetSerializer

class LinkList(generics.ListCreateAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer

class LinkDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer

class DeviceGroupList(generics.ListCreateAPIView):
    queryset = DeviceGroup.objects.all()
    serializer_class = DeviceGroupSerializer

class DeviceGroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DeviceGroup.objects.all()
    serializer_class = DeviceGroupSerializer

class VLANList(generics.ListCreateAPIView):
    queryset = VLAN.objects.all()
    serializer_class = VLANSerializer

class VLANDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = VLAN.objects.all()
    serializer_class = VLANSerializer

class DeviceEventList(generics.ListCreateAPIView):
    queryset = DeviceEvent.objects.all()
    serializer_class = DeviceEventSerializer

class DeviceEventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DeviceEvent.objects.all()
    serializer_class = DeviceEventSerializer

class RoutingTableList(generics.ListCreateAPIView):
    queryset = RoutingTable.objects.all()
    serializer_class = RoutingTableSerializer

class RoutingTableDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RoutingTable.objects.all()
    serializer_class = RoutingTableSerializer

