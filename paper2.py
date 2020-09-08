#!/usr/bin/python


"""Custom topology example

Five directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

MAC,IP, Controller, CLI stuff configured

"""

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.node import OVSSwitch, Controller, RemoteController

#It is derived from Topo Class
class MultipleSwitchesTopo(Topo):
    def build(self):
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        s5 = self.addSwitch('s5')
        s6 = self.addSwitch('s6')

        h1 = self.addHost('h1', mac="00:00:00:00:11:11", ip="192.168.1.1/24")
        h2 = self.addHost('h2', mac="00:00:00:00:11:12", ip="192.168.1.2/24")
        h3 = self.addHost('h3', mac="00:00:00:00:11:13", ip="192.168.1.3/24")


        self.addLink(s1, s2)
        self.addLink(s2, s3)
        self.addLink(s3, s4)
        self.addLink(s4, s5)
        self.addLink(s2, s6)

        self.addLink(h1, s6)
        self.addLink(h2, s5)
        self.addLink(h3, s6)


if __name__ == '__main__':
    setLogLevel('info')
    topo = MultipleSwitchesTopo()
    c1 = RemoteController('c1', ip='127.0.0.1')
    net = Mininet(topo=topo, controller=c1)
    net.start()
    net.pingAll()
    CLI(net)
    net.stop()
