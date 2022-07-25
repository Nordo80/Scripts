from scrapli.driver.core import IOSXEDriver
from scrapli.driver.core import IOSXRDriver
import re
import json
import csv

filename = "project1.csv"

list_list = []
extra_list = []

devices = [{
    "host":"ios-xe-mgmt-latest.cisco.com",
    "auth_username":"developer",
    "auth_password":"C1sco12345",
    "port":22,
    "auth_strict_key":False
}, {
    "host":"sbx-iosxr-mgmt.cisco.com",
    "auth_username":"admin",
    "auth_password":"C1sco12345",
    "port":8181,
    "auth_strict_key":False
}, {
    "host":"ios-xe-mgmt-latest.cisco.com",
    "auth_username":"developer",
    "auth_password":"C1sco12345",
    "port":22,
    "auth_strict_key":False
}]
print("----------XE-LOADING-----------")
conn_XE = IOSXEDriver(**devices[0])
conn_XE.open()
response = conn_XE.send_command("show run")
print("1) " + str(re.findall("hostname.+", response.result)[0]))
list_list.append(re.findall("hostname.+", response.result))


response = conn_XE.send_command("show hosts")
print("2) " + str(re.findall("Default.+", response.result)[0]))
list_list.append(re.findall("Default.+", response.result))


response = conn_XE.send_command("show run")
print("3) " + str(re.findall("Last.+", response.result)[0]))
list_list.append(re.findall("Last.+", response.result))


response = conn_XE.send_command("sh version")
print("4) " + str(re.findall("uptime is.+", response.result)[0]))
list_list.append(re.findall("uptime is.+", response.result))

response = conn_XE.send_command("show ip interface brief")
i = 0
for a in response.result.split():
    i += 1
i = (i / 6) - 1
print("5) Device has " + str(int(i)) + " interfaces")
extra_list.append("Device has " + str(int(i)) + " interfaces")
list_list.append(extra_list)
extra_list = []

json_up_interfaces = json.dumps(re.findall(".+up.+", response.result), indent = 2)
print("6) " + str(int(json_up_interfaces.count(',')) + 1) + " interfaces are enabled\n")
extra_list.append(str(int(json_up_interfaces.count(',')) + 1) + " interfaces are enabled")
list_list.append(extra_list)
extra_list = []

response = conn_XE.send_command("show ip interface brief")

print("--------INTERFACE TABLE---------------")
response1 = conn_XE.send_command("show interfaces")
mac_address = re.findall(", address is.+", response1.result)
parsed = response.genie_parse_output()
counter = 0
for interface in parsed.values():
    for name, ip_addr in interface.items():
        if counter <= len(mac_address) - 1:
            print(name + " " + ip_addr['ip_address'] + " MAC" + str(mac_address[counter]))
            extra_list.append(name + " " + ip_addr['ip_address'] + " MAC" + str(mac_address[counter]))
            list_list.append(extra_list)
            extra_list = []
            counter += 1
        else:
            print(name + " " + ip_addr['ip_address'])
            extra_list.append(name + " " + ip_addr['ip_address'])
            list_list.append(extra_list)
            extra_list = []
        
print("--------------------------------------\n")
    

response = conn_XE.send_command("show ip ssh")
print("\n" + str(re.findall("SSH.+", response.result)[0]))
extra_list.append(re.findall("SSH.+", response.result))
list_list.append(extra_list)
extra_list = []

response = conn_XE.send_command("show users")

f = 0
parsed = response.genie_parse_output()
for interface in parsed.values():
    for name, value in interface.items():
        f += 1
        print(name + " " + value['location'])
        extra_list.append(name + " " + value['location'])
        list_list.append(extra_list)
        extra_list = []

"""for interface in parsed.values():
    for name, ip_addr in interface.items()
        print(name + " " + ip_addr["""        
"""json_up_interfaces = json.dumps(re.findall("vty.+", response.result), indent = 2)
print(json_up_interfaces)"""


print("\n" + str(int(f)) + " SSH sessions are currently open\n")
extra_list.append(str(int(f)) + " SSH sessions are currently open")
list_list.append(extra_list)
extra_list = []

response = conn_XE.send_command("show ip traffic")
receive = re.search("Rcvd.+", response.result)
print(receive.group(0))
extra_list.append(receive.group(0))
list_list.append(extra_list)
extra_list = []

sent = re.search("Sent.+", response.result)
print(sent.group(0))
extra_list.append(sent.group(0))
list_list.append(extra_list)
extra_list = []
conn_XE.close()

print("----------XR-LOADING-----------")


conn_XR = IOSXRDriver(**devices[1])
conn_XR.open()
list_list.append(extra_list)
extra_list = []

response = conn_XR.send_command("show run")
print("1) " + str(re.findall("hostname.+", response.result)[0]))
list_list.append(re.findall("hostname.+", response.result))


response = conn_XR.send_command("show hosts")
print("2) " + str(re.findall("Default.+", response.result)[0]))
list_list.append(re.findall("Default.+", response.result))


response = conn_XR.send_command("show run")
print("3) " + str(re.findall("Last.+", response.result)[0]))
list_list.append(re.findall("Last.+", response.result))


response = conn_XR.send_command("sh version")
print("4) " + str(re.findall("uptime is.+", response.result)[0]))
list_list.append(re.findall("uptime is.+", response.result))

response = conn_XR.send_command("show ip interface brief")
i = 0
for a in response.result.split():
    i += 1
i = (i / 6) - 1
print("5) Device has " + str(int(i)) + " interfaces")
extra_list.append("Device has " + str(int(i)) + " interfaces")
list_list.append(extra_list)
extra_list = []

json_up_interfaces = json.dumps(re.findall(".+up.+", response.result), indent = 2)
print("6) " + str(int(json_up_interfaces.count(',')) + 1) + " interfaces are enabled\n")
extra_list.append(str(int(json_up_interfaces.count(',')) + 1) + " interfaces are enabled")
list_list.append(extra_list)
extra_list = []

response = conn_XR.send_command("show ip interface brief")

print("--------INTERFACE TABLE---------------")
response1 = conn_XR.send_command("show interfaces")
mac_address = re.findall(", address is.+", response1.result)
parsed = response.genie_parse_output()
counter = 0
for interface in parsed.values():
    for name, ip_addr in interface.items():
        if counter <= len(mac_address) - 1:
            print(name + " " + ip_addr['ip_address'] + " MAC" + str(mac_address[counter]))
            extra_list.append(name + " " + ip_addr['ip_address'] + " MAC" + str(mac_address[counter]))
            list_list.append(extra_list)
            extra_list = []
            counter += 1
        else:
            print(name + " " + ip_addr['ip_address'])
            extra_list.append(name + " " + ip_addr['ip_address'])
            list_list.append(extra_list)
            extra_list = []
        
print("--------------------------------------\n")
    

response = conn_XR.send_command("show ip ssh")
print("\n" + str(re.findall("SSH.+", response.result)[0]))
extra_list.append(re.findall("SSH.+", response.result))
list_list.append(extra_list)
extra_list = []

response = conn_XR.send_command("show users")

f = 0
parsed = response.genie_parse_output()
for interface in parsed.values():
    for name, value in interface.items():
        f += 1
        print(name + " " + value['location'])
        extra_list.append(name + " " + value['location'])
        list_list.append(extra_list)
        extra_list = []


print("\n" + str(int(f)) + " SSH sessions are currently open\n")
extra_list.append(str(int(f)) + " SSH sessions are currently open")
list_list.append(extra_list)
extra_list = []

response = conn_XR.send_command("show ip traffic")
receive = re.search("Rcvd.+", response.result)
print(receive.group(0))
extra_list.append(receive.group(0))
list_list.append(extra_list)
extra_list = []

sent = re.search("Sent.+", response.result)
print(sent.group(0))
extra_list.append(sent.group(0))
list_list.append(extra_list)
extra_list = []
conn_XR.close()

print("----------XE-LOADING-----------")
conn_XE = IOSXEDriver(**devices[2])
conn_XE.open()
response = conn_XE.send_command("show run")
print("1) " + str(re.findall("hostname.+", response.result)[0]))
list_list.append(re.findall("hostname.+", response.result))


response = conn_XE.send_command("show hosts")
print("2) " + str(re.findall("Default.+", response.result)[0]))
list_list.append(re.findall("Default.+", response.result))


response = conn_XE.send_command("show run")
print("3) " + str(re.findall("Last.+", response.result)[0]))
list_list.append(re.findall("Last.+", response.result))


response = conn_XE.send_command("sh version")
print("4) " + str(re.findall("uptime is.+", response.result)[0]))
list_list.append(re.findall("uptime is.+", response.result))

response = conn_XE.send_command("show ip interface brief")
i = 0
for a in response.result.split():
    i += 1
i = (i / 6) - 1
print("5) Device has " + str(int(i)) + " interfaces")
extra_list.append("Device has " + str(int(i)) + " interfaces")
list_list.append(extra_list)
extra_list = []

json_up_interfaces = json.dumps(re.findall(".+up.+", response.result), indent = 2)
print("6) " + str(int(json_up_interfaces.count(',')) + 1) + " interfaces are enabled\n")
extra_list.append(str(int(json_up_interfaces.count(',')) + 1) + " interfaces are enabled")
list_list.append(extra_list)
extra_list = []

response = conn_XE.send_command("show ip interface brief")

print("--------INTERFACE TABLE---------------")
response1 = conn_XE.send_command("show interfaces")
mac_address = re.findall(", address is.+", response1.result)
parsed = response.genie_parse_output()
counter = 0
for interface in parsed.values():
    for name, ip_addr in interface.items():
        if counter <= len(mac_address) - 1:
            print(name + " " + ip_addr['ip_address'] + " MAC" + str(mac_address[counter]))
            extra_list.append(name + " " + ip_addr['ip_address'] + " MAC" + str(mac_address[counter]))
            list_list.append(extra_list)
            extra_list = []
            counter += 1
        else:
            print(name + " " + ip_addr['ip_address'])
            extra_list.append(name + " " + ip_addr['ip_address'])
            list_list.append(extra_list)
            extra_list = []
        
print("--------------------------------------\n")
    

response = conn_XE.send_command("show ip ssh")
print("\n" + str(re.findall("SSH.+", response.result)[0]))
extra_list.append(re.findall("SSH.+", response.result))
list_list.append(extra_list)
extra_list = []

response = conn_XE.send_command("show users")

f = 0
parsed = response.genie_parse_output()
for interface in parsed.values():
    for name, value in interface.items():
        f += 1
        print(name + " " + value['location'])
        extra_list.append(name + " " + value['location'])
        list_list.append(extra_list)
        extra_list = []

"""for interface in parsed.values():
    for name, ip_addr in interface.items()
        print(name + " " + ip_addr["""        
"""json_up_interfaces = json.dumps(re.findall("vty.+", response.result), indent = 2)
print(json_up_interfaces)"""


print("\n" + str(int(f)) + " SSH sessions are currently open\n")
extra_list.append(str(int(f)) + " SSH sessions are currently open")
list_list.append(extra_list)
extra_list = []

response = conn_XE.send_command("show ip traffic")
receive = re.search("Rcvd.+", response.result)
print(receive.group(0))
extra_list.append(receive.group(0))
list_list.append(extra_list)
extra_list = []

sent = re.search("Sent.+", response.result)
print(sent.group(0))
extra_list.append(sent.group(0))
list_list.append(extra_list)
extra_list = []
conn_XE.close()


with open(filename, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(list_list)
