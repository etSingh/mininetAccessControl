#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call

def myNetwork():

    net = Mininet( topo=None,           # net is a Mininet() object
                   build=False,
                   ipBase='10.0.0.0/8')

    info( '*** Adding controller\n' )
    c0=net.addController(name='c0',
                      controller=RemoteController,
                      protocol='tcp',
                      port=6633)

    info( '*** Add switches\n') 
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch) # s1 is a switch object

    info( '*** Add hosts\n')
    h4 = net.addHost('h4', cls=Host, ip='10.0.0.4', defaultRoute=None)
    h3 = net.addHost('h3', cls=Host, ip='10.0.0.3', defaultRoute=None)
    h2 = net.addHost('h2', cls=Host, ip='10.0.0.2', defaultRoute=None)
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None)

    info( '*** Add NAT\n')
    nat = net.addNAT( 'nat', connect=True, inNamespace=False, ip='10.0.0.254' )
    
    info( '*** Add links\n')
    net.addLink(h1, s1)      # creates a Link() object
    net.addLink(h4, s1)
    net.addLink(h2, s1)
    net.addLink(h3, s1)
    net.addLink(nat, s1) 

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('s1').start([c0])

    info( '*** Post configure switches and hosts\n')
    startServer(h4) 
    hosts = [h1, h2, h3, h4]
    setMacAddress(hosts)
    printInfo(hosts)
    CLI(net)
    stopServer(h4)
    net.stop()

def startServer(h):
    h.cmd( 'python -m SimpleHTTPServer 80 &' )
    print ( h, ':Server running on port 80' )

def stopServer(h):
    h.cmd( 'kill %python' )

def setMacAddress(hosts):
    a = 42
    address=''
    for h in hosts:
        for x in range(6):
            address += str(a) + ':' 
        h.setMAC(address)
        a += 1
        address=''

def printInfo(hosts):
    for h in hosts:
        print "Host", h.name, "has IP address", h.IP(), "and MAC address", h.MAC()
    

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()

