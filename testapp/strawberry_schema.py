import strawberry
from strawberry import auto
from strawberry.django import mutations
from strawberry_django.optimizer import DjangoOptimizerExtension

from .models import (
    NetworkDevice, Interface, Subnet, Link,
    DeviceGroup, VLAN, DeviceEvent, RoutingTable
)

# -------------------- Types --------------------
@strawberry.django.type(NetworkDevice)
class NetworkDeviceType:
    id: auto
    name: auto
    device_type: auto
    ip_address: auto
    interfaces: list["InterfaceType"]
    subnets: list["SubnetType"]
    routing_tables: list["RoutingTableType"]

@strawberry.django.type(Interface)
class InterfaceType:
    id: auto
    name: auto
    device: NetworkDeviceType
    ip_address: auto
    mac_address: auto

@strawberry.django.type(Subnet)
class SubnetType:
    id: auto
    network_device: NetworkDeviceType
    network_address: auto
    netmask: auto

@strawberry.django.type(Link)
class LinkType:
    id: auto
    device_1: NetworkDeviceType
    device_2: NetworkDeviceType
    bandwidth: auto
    status: auto

@strawberry.django.type(DeviceGroup)
class DeviceGroupType:
    id: auto
    name: auto
    devices: list[NetworkDeviceType]

@strawberry.django.type(VLAN)
class VLANType:
    id: auto
    vlan_id: auto
    name: auto
    devices: list[NetworkDeviceType]

@strawberry.django.type(DeviceEvent)
class DeviceEventType:
    id: auto
    device: NetworkDeviceType
    event_type: auto
    timestamp: auto

@strawberry.django.type(RoutingTable)
class RoutingTableType:
    id: auto
    network_device: NetworkDeviceType
    destination_network: auto
    gateway: auto
    netmask: auto
    metric: auto

# -------------------- Queries --------------------
@strawberry.type
class Query:
    # Network Devices
    network_devices: list[NetworkDeviceType] = strawberry.django.field()
    network_device: NetworkDeviceType = strawberry.django.field()

    # Interfaces
    interfaces: list[InterfaceType] = strawberry.django.field()
    interface: InterfaceType = strawberry.django.field()

    # Subnets
    subnets: list[SubnetType] = strawberry.django.field()
    subnet: SubnetType = strawberry.django.field()

    # Links
    links: list[LinkType] = strawberry.django.field()
    link: LinkType = strawberry.django.field()

    # Device Groups
    device_groups: list[DeviceGroupType] = strawberry.django.field()
    device_group: DeviceGroupType = strawberry.django.field()

    # VLANs
    vlans: list[VLANType] = strawberry.django.field()
    vlan: VLANType = strawberry.django.field()

    # Device Events
    device_events: list[DeviceEventType] = strawberry.django.field()
    device_event: DeviceEventType = strawberry.django.field()

    # Routing Tables
    routing_tables: list[RoutingTableType] = strawberry.django.field()
    routing_table: RoutingTableType = strawberry.django.field()

# -------------------- Mutations --------------------
@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_network_device(
        self,
        name: str,
        device_type: str,
        ip_address: str
    ) -> NetworkDeviceType:
        return NetworkDevice.objects.create(
            name=name,
            device_type=device_type,
            ip_address=ip_address
        )

    @strawberry.mutation
    def update_network_device(
        self,
        id: int,
        name: str | None = None,
        device_type: str | None = None,
        ip_address: str | None = None
    ) -> NetworkDeviceType:
        device = NetworkDevice.objects.get(pk=id)
        if name: device.name = name
        if device_type: device.device_type = device_type
        if ip_address: device.ip_address = ip_address
        device.save()
        return device

    @strawberry.mutation
    def delete_network_device(self, id: int) -> bool:
        NetworkDevice.objects.get(pk=id).delete()
        return True

    # Add similar mutations for other models...

# DjangoOptimizierExtension solves N+1 problem for following query:
"""
query MyQuery {
  deviceGroups {
    devices {
      id
      deviceType
      interfaces {
        id
        device {
          deviceType
          ipAddress
        }
      }
    }
  }
}
"""
strawberry_schema = strawberry.Schema(query=Query, mutation=Mutation, extensions=[DjangoOptimizerExtension])
