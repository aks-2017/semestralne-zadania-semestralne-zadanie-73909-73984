#!/usr/bin/python

import time
import json
import argparse
from time import sleep
import os
import re
import sys
import argparse
from mininet.node import Node
from mininet.cli import CLI
from mininet.topolib import TreeTopo
from mininet.util import quietRun
from mininet.topo import Topo
from minisched import scheduler
from mininet.topo import SingleSwitchTopo
from mininet.log import setLogLevel, info, debug,error
from mininet.net import Mininet
from mininet.node import OVSController, DefaultController, Host, OVSKernelSwitch
from mininet.link import TCLink, Intf, Link


class Min( Topo ):
    def build( self ):
        s1=self.addSwitch('s1')
	s2=self.addSwitch('s2')
	self.addLink(s1,s2)

class Minievents(Mininet):
    def __init__(self, topo=None, switch=OVSKernelSwitch, host=Host,
                 controller=DefaultController, link=Link, intf=Intf,
                 build=True, xterms=False, cleanup=False, ipBase='10.0.0.0/8',
                 inNamespace=False,
                 autoSetMacs=False, autoStaticArp=False, autoPinCpus=False,
                 listenPort=None, waitConnected=False, events_file=None):
        super(Minievents, self).__init__(topo=topo, switch=switch, host=host, controller=controller,
                                         link=link, intf=intf, build=build, xterms=xterms, cleanup=cleanup,
                                         ipBase=ipBase, inNamespace=inNamespace, autoSetMacs=autoSetMacs,
                                         autoStaticArp=autoStaticArp, autoPinCpus=autoPinCpus,
                                         listenPort=listenPort,
                                         waitConnected=waitConnected)

        self.scheduler = scheduler(time.time, time.sleep)
        if events_file:
            json_events = json.load(open(events_file))
            self.load_events(json_events)

    def load_events(self, json_events):

        event_type_to_f = {'editLink': self.editLink}
        for event in json_events:
            debug("processing event: time {time}, type {type}, params {params}\n".format(**event))
            event_type = event['type']
            self.scheduler.enter(event['time'], 1, event_type_to_f[event_type], kwargs=event['params'])

    def editLink(self, **kwargs):
        n1, n2 = self.get(kwargs['src'], kwargs['dst'])
        intf_pairs = n1.connectionsTo(n2)
        info('***editLink event at t={time}: {args}\n'.format(time=time.time(), args=kwargs))
        for intf_pair in intf_pairs:
            n1_intf, n2_intf = intf_pair
            n1_intf.config(**kwargs)
            n2_intf.config(**kwargs)

    def start(self):
        super(Minievents, self).start()
        CLI(self) if self.scheduler.empty() else self.scheduler.run()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--events",default="bw.json", help="json file with event descriptions")
    args = parser.parse_args()
    setLogLevel('info')
    net = Minievents( topo=Min( ),link=TCLink, events_file=args.events)
    s1 = net.switches[0]
    s2 = net.switches[1]
    _intf = Intf( 'eth0', node=s1)
    _intf = Intf( 'eth2', node=s2)
    net.start()
    CLI( net )
    net.stop()

