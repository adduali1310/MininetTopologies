#!/usr/bin/python


"""Custom topology 

According to the Figure 1 in https://www.cs.rice.edu/~angchen/papers/sigcomm-2016.pdf

"""

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.node import OVSSwitch, Controller, RemoteController

#It is derived from Topo Class
class ReadComponents(Topo):
    def build(self):
        hosts=[]
        switches=[]
        
        with open('/home/adnan/MininetTopologies/components2.txt') as filehandle:
                #lines = f.read().splitlines()
                #lines = f.readline()
                #print(lines)
                try:
                    for line in filehandle:
                        line=line.rstrip("\n")
                        if "Clients" in line:
                            clients=line.split("Clients=",1)[1].split(" ")
                            for client in clients:
                                host=client.split("(")[0]
                                ipaddr=client.split("(")[1].replace(")","")
                                hosts.append(self.addHost(host, ip=ipaddr))  
                        elif "Switches" in line:
                            switch=line.split("Switches=",1)[1].split(" ")
                            for component in switch:
                                switches.append(self.addSwitch(component))
                        elif "Switch-SwitchLink" in line:
                            link=line.split("Switch-SwitchLink=",1)[1].split(" ")
                            for item in link:
                                leftSwitchindex=int(item[1:-1].split(",")[0])
                                rightSwitchindex=int(item[1:-1].split(",")[1])
                                self.addLink(switches[leftSwitchindex-1],switches[rightSwitchindex-1])
                        elif "Client-SwitchLink" in line:
                            link=line.split("Client-SwitchLink=",1)[1].split(" ")
                            for item in link:
                                clientindex=int(item[1:-1].split(",")[0])
                                switchindex=int(item[1:-1].split(",")[1])
                                self.addLink(hosts[clientindex-1],switches[switchindex-1])
                                
                        else:
                            continue
                finally:
                    filehandle.close()

 



if __name__ == '__main__':
    setLogLevel('info')
    topo = ReadComponents()
    c1 = RemoteController('c1', ip='127.0.0.1')
    net = Mininet(topo=topo, controller=c1 ,autoSetMacs=True)
    net.start()
    #net.pingAll()
    #Another way To Access Components
    #sw1=net.get('sw1')
    #print(sw1.IP())
    CLI(net)
    net.stop()
