import random
from datetime import datetime
from django.utils import timezone
from testapp.models import NetworkDevice, Interface, Subnet, Link, DeviceGroup, VLAN, DeviceEvent, RoutingTable

def create_batch_of_network_data(batch_size=1000):
    """
    Creates a batch of network-related models for performance testing.
    """
    # Step 1: Create a batch of NetworkDevices
    devices = []
    for i in range(batch_size):
        device = NetworkDevice.objects.create(
            name=f"Device-{i}",
            device_type=random.choice(['Router', 'Switch']),
            ip_address=f"192.168.1.{i + 1}"
        )
        devices.append(device)

    # Step 2: Create Interfaces for each NetworkDevice
    interfaces = []
    for device in devices:
        for j in range(2):  # 2 interfaces per device (example)
            interface = Interface.objects.create(
                name=f"{device.name}-eth{j+1}",
                device=device,
                ip_address=f"192.168.{i + 1}.{j + 10}",
                mac_address=f"{random.randint(0, 255):02x}:{random.randint(0, 255):02x}:{random.randint(0, 255):02x}:{random.randint(0, 255):02x}:{random.randint(0, 255):02x}:{random.randint(0, 255):02x}"
            )
            interfaces.append(interface)

    # Step 3: Create Subnets for each NetworkDevice
    subnets = []
    for device in devices:
        subnet = Subnet.objects.create(
            network_device=device,
            network_address=f"192.168.{random.randint(0, 255)}.0",
            netmask="255.255.255.0"
        )
        subnets.append(subnet)

    # Step 4: Create Links between pairs of NetworkDevices
    links = []
    for i in range(batch_size // 2):
        link = Link.objects.create(
            device_1=devices[i],
            device_2=devices[batch_size - i - 1],
            bandwidth=random.randint(100, 1000),  # Random bandwidth between 100-1000 Mbps
            status=random.choice([True, False])
        )
        links.append(link)

    # Step 5: Create DeviceGroups (with some overlap)
    groups = []
    for i in range(batch_size // 10):  # Create 10 groups
        group = DeviceGroup.objects.create(
            name=f"Group-{i}"
        )
        group.devices.add(*random.sample(devices, 5))  # Add 5 random devices to the group
        groups.append(group)

    # Step 6: Create VLANs (with some overlap)
    vlans = []
    for i in range(batch_size // 20):  # Create 50 VLANs
        vlan = VLAN.objects.create(
            vlan_id=random.randint(100, 500),
            name=f"VLAN-{i}"
        )
        vlan.devices.add(*random.sample(devices, 5))  # Add 5 random devices to the VLAN
        vlans.append(vlan)

    # Step 7: Create Device Events for each NetworkDevice
    events = []
    for device in devices:
        for j in range(5):  # 5 events per device (example)
            event = DeviceEvent.objects.create(
                device=device,
                event_type=random.choice(['Up', 'Down', 'Reboot']),
                timestamp=timezone.now() - timezone.timedelta(days=random.randint(0, 30))
            )
            events.append(event)

    # Step 8: Create Routing Tables for each NetworkDevice
    routing_tables = []
    for device in devices:
        for j in range(3):  # 3 routing entries per device (example)
            route = RoutingTable.objects.create(
                network_device=device,
                destination_network=f"192.168.{random.randint(0, 255)}.0",
                gateway=f"192.168.{random.randint(0, 255)}.1",
                netmask="255.255.255.0",
                metric=random.randint(1, 20)
            )
            routing_tables.append(route)

    print(f"Batch of {batch_size} devices and related models created successfully!")

# Call the function to create data
create_batch_of_network_data(batch_size=1000)
