import netifaces
some = netifaces.interfaces()

for addr in some:
    print(addr)

""""
from netifaces import interfaces, ifaddreses, AF_INET

for ifaceName in interfaces():
    addresses = [i['addr'] for i in ifaddreses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}])]
    print(f"{ifaceName} {addresses}")
    """

stuffs = netifaces.ifaddresses('DCEFE177-6BFA-42CF-A638-9562A9F4F11A')
print(stuffs)