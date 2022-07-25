from suds.client import Client

client = Client('http://localhost:8000/?wsdl', cache=None)

print(client.service.ping_host("www.runescape.com"))
print(client.service.dns_host("google.com"))
print(client.service.drive_size("/"))
