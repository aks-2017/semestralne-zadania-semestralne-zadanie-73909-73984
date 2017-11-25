#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.link import Intf
from mininet.log import setLogLevel, info

#sudo -E python topologia.py
#sudo ryu-manager simple_switch.py

def myNetwork():

	net = Mininet(topo=None, build=True)

	info('*** controller\n')
	net.addController(name='c0', controller=RemoteController)

	info('*** switch\n')
	s1 = net.addSwitch('s1')
	Intf('eth0', node=s1)
	Intf('eth2', node=s1)

	info('*** starting')
	net.start()
	CLI(net)
	net.stop()

if __name__ == '__main__':
	setLogLevel('info')
	myNetwork()


