from rest_framework import serializers
from .models import (
    NetworkDevice, Interface, Subnet, Link, DeviceGroup, VLAN, DeviceEvent, RoutingTable
)

class NetworkDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkDevice
        fields = '__all__'

class InterfaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interface
        fields = '__all__'

class SubnetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subnet
        fields = '__all__'

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = '__all__'

class DeviceGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceGroup
        fields = '__all__'

class VLANSerializer(serializers.ModelSerializer):
    class Meta:
        model = VLAN
        fields = '__all__'

class DeviceEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceEvent
        fields = '__all__'

class RoutingTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoutingTable
        fields = '__all__'
