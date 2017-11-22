#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.link import Intf
from mininet.log import setLogLevel, info

def myNetwork():

	net = Mininet(topo=None, build=False)

	info('*** controller\n')
	net.addController(name='c0', controller=RemoteController)

	info('*** switch\n')
	s1 = net.addSwitch('s1')
	Intf('eth1', node=s1)

	info('*** host\n')
	h1 = net.addHost('h1', ip = '0.0.0.0')

	info('*** link\n')
	net.addLink(h1, s1)

	info('*** starting')
	net.start()
	#s1.cmdPrint('dhclient '+s1.defaultIntf().name)
	CLI(net)
	net.stop()

if __name__ == '__main__':
	setLogLevel('info')
	myNetwork()


