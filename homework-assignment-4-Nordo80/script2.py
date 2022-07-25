import dns
import dns.resolver

def dns_host(host):
  i = 1
  ns = dns.resolver.query(host, 'NS')
  print(f"The Name Servers (NS) of {host}: ")
  for lala in ns:
    print(i, lala.to_text())
    i+=1
  ip = dns.resolver.query(host, 'A')
  for lala in ip:
    print(f"\nThe DNS A Record of {host}:\n" + lala.to_text())

  result = dns.resolver.query(host, 'MX')
  print(f"\nThe MX Records of {host}:")
  for lala in result:
    print(lala.to_text())
dns_host("google.com")


