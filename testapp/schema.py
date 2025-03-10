import graphene
from graphene_django.types import DjangoObjectType
from .models import NetworkDevice, Interface, Subnet, Link, DeviceGroup, VLAN, DeviceEvent, RoutingTable
from query_optimizer import DjangoObjectType, DjangoListField

# Define DjangoObjectTypes for each model

class NetworkDeviceType(DjangoObjectType):
    class Meta:
        model = NetworkDevice

class InterfaceType(DjangoObjectType):
    class Meta:
        model = Interface

class SubnetType(DjangoObjectType):
    class Meta:
        model = Subnet

class LinkType(DjangoObjectType):
    class Meta:
        model = Link

class DeviceGroupType(DjangoObjectType):
    class Meta:
        model = DeviceGroup

class VLANType(DjangoObjectType):
    class Meta:
        model = VLAN

class DeviceEventType(DjangoObjectType):
    class Meta:
        model = DeviceEvent

class RoutingTableType(DjangoObjectType):
    class Meta:
        model = RoutingTable

# Query class to fetch data

class Query(graphene.ObjectType):
    # Basic queries for fetching models
    network_devices = DjangoListField(NetworkDeviceType)
    interfaces = DjangoListField(InterfaceType)
    subnets = DjangoListField(SubnetType)
    links = DjangoListField(LinkType)
    device_groups = DjangoListField(DeviceGroupType)
    vlans = DjangoListField(VLANType)
    device_events = DjangoListField(DeviceEventType)
    routing_tables = DjangoListField(RoutingTableType)

    # Resolvers for queries
    def resolve_network_devices(self, info):
        return NetworkDevice.objects.all()

    def resolve_interfaces(self, info):
        return Interface.objects.all()

    def resolve_subnets(self, info):
        return Subnet.objects.all()

    def resolve_links(self, info):
        return Link.objects.all()

    def resolve_device_groups(self, info):
        return DeviceGroup.objects.all()

    def resolve_vlans(self, info):
        return VLAN.objects.all()

    def resolve_device_events(self, info):
        return DeviceEvent.objects.all()

    def resolve_routing_tables(self, info):
        return RoutingTable.objects.all()


schema = graphene.Schema(query=Query)
