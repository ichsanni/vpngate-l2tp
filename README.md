# vpngate-l2tp
Dirty application to connect to VPNGate servers using L2TP protocol on Windows.

## How to install
    pip install git+https://github.com/ichsanni/vpngate-l2tp.git
  
_______________________________

## How to use

Basic usage:

    from vpngate_l2tp.vpn import L2TP_VPNGate
    
    vpn = L2TP_VPNGate()
    vpn.connect()         # If not specified, will default to Japan/JP
  
Specify the country of your choice: `vpn.connect('JP')` or `vpn.connect('US')`

Get list of countries available: 

    from vpngate_l2tp.vpn import L2TP_VPNGate
    
    vpn = L2TP_VPNGate()
    print(vpn.country_abbreviation)
    # will output: ['JP', 'KR', 'RU', 'TH', 'US', 'VI'] depending on available servers from VPNGate
