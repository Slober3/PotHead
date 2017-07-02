__author__ = '@Slober3'
__version__ = '0.1'

'''
Hello Welcome to this simple low interactinghoneypot
This honepot will only log
And will not interact with the hacker at this point in time!
'''

import sys
sys.path.append('../')
import argparse
import socket
import _thread
import time


from modules.PotHeadMain import CrlogDir,prPhaseOne,prStandard,runSocketServ,logHandling
# parse the command line arguments to set the variables for the server
parser = argparse.ArgumentParser(description="Command line arguments")
parser.add_argument('-i',action='store', metavar='<ip address>', default='0.0.0.0', help='The IP address to listen on default 0.0.0.0')
parser.add_argument('-p',action='store', metavar='<port>', default='9999', help='The port to listen on default 9999')
parser.add_argument('-s',action='store', metavar='<PotHeadServer>', default='PotHead', help='A Name that\'ll show up as the VNC server name')
parser.add_argument('-logDir',action='store', metavar='<logDir>', default='logs', help='log Directory')
parser.add_argument('-motd',action='store', metavar='<motd>', default='Welcome to HMLK 612.45', help='MOTD used on this server')
parser.add_argument('-pp',action='store', metavar='<port list>',nargs='+', help='Multiple ports')
parser.add_argument('-site',action='store', metavar='<site>',default='http://7ol.eu/write.php', help='Server site')

args = parser.parse_args()

# set the IP address, Port, ServerName variables
bind_ip = args.i
bind_port = int(args.p)
srvname = args.s
motd = args.motd
logDirName = args.logDir
multiplePorts = args.pp 
site = args.site

#set Variables for Print messages
banner = ('''
*********************************************************************************************
\tPotHead - A Simple LowInteraction Thing - Version: {}
*********************************************************************************************
'''.format(__version__))


prInitPhead = 'Initializing Pothead service...\n'
prLogCr = 'Log directory created...\n'
prLogCrE = 'Log directory found...\n'
prPhOne = 'Phase 1 completed...\n'
prSrvName = 'Server name: {}\n'.format(srvname)

if args.pp is not None:
    prPort = 'Port: {}\n'.format(multiplePorts)
else:
    prPort = 'Port: {}\n'.format(bind_port)

prIP = 'IP: {}\n'.format(bind_ip)
prSite ='Site: {}\n'.format(site)
motd += '\r\n'

'''
Phase 1 Begin:
Print basic server information ip, port, servname
Create log directory if not available
'''
print (banner)
print(prInitPhead)

# Check and Create log directory if not exist
# the function ChcklogDir will only check
# and WILL NOT create a log directory if not exists

if CrlogDir(logDirName) == 0:
    #prStandard is a basic Print function
    prStandard(prLogCr)
else:
    prStandard(prLogCrE)

#Prints Basic information
prPhaseOne(prSrvName,prIP,prPort,prPhOne,prSite)
#End Phase 1

'''
Phase 2 Begin:
Initiate Socketserver
'''
#Check if multiple ports are used or a single port
if args.pp is not None:
    print('Multiple ports used')
    runSocketServ(socket.AF_INET, socket.SOCK_STREAM,  multiplePorts, socket.gethostname(), 5,4096,motd,1,site)
else:
    print('Single port used')
    runSocketServ(socket.AF_INET, socket.SOCK_STREAM,  bind_port, socket.gethostname(), 5,4096,motd,0,site)
#End Phase 2 runSocketServ(socket_family, socket_type, socket_port, socket_host, socket_max):


