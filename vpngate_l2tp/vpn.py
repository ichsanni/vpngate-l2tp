import requests
import random

from .ps import *

class VPNGate:
  def __init__(self):
    self.country_abbr = list()
    self.server_list = None

  def parse_csv(self, data):
    vpn_list = dict()

    data = data[1:-2]
    header = data.pop(0).split(',')

    for server in data:
      server = server.split(',')
      if server[6] not in vpn_list.keys():
        vpn_list[server[6]] = list()

      detail = {head:srv for head,srv in zip(header[:-1],server[:-1])}
      ls_key = vpn_list[server[6]]
      vpn_list[server[6]] = ls_key + [detail]

    self.country_abbr = vpn_list.keys()
    self.server_list = vpn_list

    return self.server_list

  def get_list_of_servers(self):
    page = requests.get('http://www.vpngate.net/api/iphone/')
    res = self.parse_csv(page.text.split('\n'))
    return res

class L2TP_Conn:
  def __init__(self):
    self.ip = None

  def create_connection(self, ip, l2tp_psk="vpn"):
    command = f'Add-VpnConnection -Name VPNGate-L2TP -ServerAddress {ip} -TunnelType L2tp -L2tpPsk {l2tp_psk} -Force'
    try: run(command)
    except RuntimeError:
      command = f'Set-VpnConnection -Name VPNGate-L2TP -ServerAddress {ip} -TunnelType L2tp -L2tpPsk {l2tp_psk} -Force'
      run(command)
    self.ip = ip

  def connect_vpn(self, username="vpn", password="vpn", vpn_name="VPNGate-L2TP"):
    command = f"rasdial {vpn_name} {username} {password}"
    run(command)

  def disconnect_vpn(self, vpn_name="VPNGate-L2TP"):
    command = f"rasdial {vpn_name} /disconnect"
    run(command)

class L2TP_VPNGate:
  def __init__(self):
    vpngate = VPNGate()
    self.server_list = vpngate.get_list_of_servers()
    self.country_abbreviation = [x for x in vpngate.country_abbr]
    self.l2tp = L2TP_Conn()

  def find_server(self, country='JP'):
    if country not in self.country_abbreviation:
      print('Country not in server lists, attempting to connect to random server.')
      country = random.choice(self.country_abbreviation)
    else:
      country = country

    server = random.choice(self.server_list[country])
    return server

  def connect(self, country='JP'):
    print('Finding a server...')
    the_chosen_one = self.find_server(country)
    print(f'Connecting to country {the_chosen_one["CountryShort"]}: {the_chosen_one["IP"]}:443, ')
    self.l2tp.create_connection(the_chosen_one['IP'], l2tp_psk='vpn')
    self.l2tp.connect_vpn('vpn', 'vpn')

  def disconnect(self):
    self.l2tp.disconnect_vpn()
    print('VPN disconnected.')

  def get_countries(self):
    return self.country_abbreviation


if __name__=='__main__':
  vpn = L2TP_VPNGate()
  vpn.connect('JP')
  # vpn.disconnect()