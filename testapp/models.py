from django.db import models


class NetworkDevice(models.Model):
    name = models.CharField(max_length=100)
    device_type = models.CharField(max_length=50)  # e.g., 'Router', 'Switch'
    ip_address = models.GenericIPAddressField()

    def __str__(self):
        return self.name

class Interface(models.Model):
    name = models.CharField(max_length=50)
    device = models.ForeignKey(NetworkDevice, related_name='interfaces', on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField()
    mac_address = models.CharField(max_length=17)

    def __str__(self):
        return f"{self.device.name} - {self.name}"

class Subnet(models.Model):
    network_device = models.ForeignKey(NetworkDevice, related_name='subnets', on_delete=models.CASCADE)
    network_address = models.GenericIPAddressField()
    netmask = models.GenericIPAddressField()

    def __str__(self):
        return f"{self.network_address}/{self.netmask}"

class Link(models.Model):
    device_1 = models.ForeignKey(NetworkDevice, related_name='outgoing_links', on_delete=models.CASCADE)
    device_2 = models.ForeignKey(NetworkDevice, related_name='incoming_links', on_delete=models.CASCADE)
    bandwidth = models.IntegerField()  # Mbps
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"Link between {self.device_1.name} and {self.device_2.name}"

class DeviceGroup(models.Model):
    name = models.CharField(max_length=100)
    devices = models.ManyToManyField(NetworkDevice, related_name='groups')

class VLAN(models.Model):
    vlan_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    devices = models.ManyToManyField(NetworkDevice, related_name='vlans')

class DeviceEvent(models.Model):
    device = models.ForeignKey(NetworkDevice, related_name='events', on_delete=models.CASCADE)
    event_type = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

class RoutingTable(models.Model):
    network_device = models.ForeignKey(NetworkDevice, related_name='routing_tables', on_delete=models.CASCADE)
    destination_network = models.GenericIPAddressField()
    gateway = models.GenericIPAddressField()
    netmask = models.GenericIPAddressField()
    metric = models.IntegerField()

    def __str__(self):
        return f"Route for {self.network_device.name} to {self.destination_network}"

