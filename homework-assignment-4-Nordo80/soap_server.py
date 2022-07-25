from spyne import Application, rpc, ServiceBase, Iterable, Integer, Unicode, String

from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
import dns
import dns.resolver
import subprocess
import platform
import netifaces as ni
import shutil
from colors import blue
import shutil
from hurry.filesize import size
from hurry.filesize import alternative


class HelloWorldService(ServiceBase):
    @rpc(Unicode, _returns=String())
    def ping_host(ctx, host):
        ping_string = ""
        ping_string += "I am using " + str(platform.system()) + " Platform \n"
        ip = ni.ifaddresses('enp0s8')[ni.AF_INET][0]['addr']
        ping_string += "My IP address" + " is " + str(ip) + "\n"
        response = subprocess.call(
            ['ping', '-c', '1', host], stdout=subprocess.DEVNULL)
        if response == 0:
            ping_string += "and " + host + " is" + " reachable \n"
        else:
            ping_string += "and " + host + " is not reachable \n"

        return ping_string


    @rpc(Unicode, _returns=String())
    def dns_host(ctx, host):
        new_string = ""
        i = 1
        ns = dns.resolver.query(host, 'NS')
        new_string += f"The Name Servers (NS) of {host}: \n"
        for lala in ns:
            new_string += str(i) + " " + str(lala.to_text() + "\n")
            i += 1
        ip = dns.resolver.query(host, 'A')
        for lala in ip:
            new_string += f"\nThe DNS A Record of {host}:\n" + lala.to_text() + "\n"

        result = dns.resolver.query(host, 'MX')
        new_string += f"\nThe MX Records of {host}: \n"
        for lala in result:
            new_string += lala.to_text() + "\n"
        return new_string


    @rpc(Unicode, _returns=String())
    def drive_size(ctx, drive):
        total, used, free = shutil.disk_usage(drive)
        drive_string = ""
        drive_string += "Total: " + size(total, system = alternative) + "\n"
        drive_string += "Used: " + size(used, system = alternative) + "\n"
        drive_string += "Free: " + size(free, system = alternative) + "\n"
        return drive_string


application = Application([HelloWorldService], 'spyne.examples.hello.soap',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

wsgi_application = WsgiApplication(application)


if __name__ == '__main__':
    import logging

    from wsgiref.simple_server import make_server

    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('spyne.protocol.xml').setLevel(logging.DEBUG)

    logging.info("listening to http://127.0.0.1:8000")
    logging.info("wsdl is at: http://localhost:8000/?wsdl")

    server = make_server('127.0.0.1', 8000, wsgi_application)
    server.serve_forever()
