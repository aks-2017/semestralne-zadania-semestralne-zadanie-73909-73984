#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.link import Intf, TCLink
from mininet.log import setLogLevel, info
from mininet.topo import Topo
from functools import partial

def myNetwork():
        link = partial(TCLink, bw=1)
        net = Mininet(topo=None, build=True, link=link)
        info('*** controller\n')
        net.addController(name='c0', controller=RemoteController)
        info('*** switch\n')
        s1 = net.addSwitch('s1')
        s2 = net.addSwitch('s2')
        Intf('eth0', node=s1)
        Intf('eth2', node=s2)
        net.addLink(s1, s2)
        info('*** starting')
        net.start()
        CLI(net)
        net.stop()

if __name__ == '__main__':
        setLogLevel('info')
        myNetwork()
