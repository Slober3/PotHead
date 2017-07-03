'''
PotHead main module
Contains the main modules
'''
import os
import socket
import _thread
import time
import select
import urllib.parse,urllib.request
from datetime import datetime

#Check if log directory exists
def ChcklogDir(logDirName):
    if not os.path.isdir(logDirName):
        return 0
    else:
        return 1

#Create Log dir
def CrlogDir(logDirName):
    if ChcklogDir(logDirName) == 0:
        os.mkdir(logDirName)
        return 0
    else:
        return 1

#Print relevant info for Phase one (servername, IP, port, information)
def prPhaseOne(prSrvName,prIP,prPort,prPhOne,prSite):
    print(prSrvName)
    print(prIP)
    print(prPort)
    print (prPhOne)
    print (prSite)

#Print standard information
def prStandard(prSt):
    print (prSt)

#Socket server and handling
def crSocketServ(socket_family, socket_type, socket_port, socket_host, socket_max, socket_buff_max,motd, site,apikey):
    srvSocket = socket.socket (socket_family, socket_type)
    srvSocket.bind((socket_host,socket_port))
    srvSocket.listen(socket_max)
    monitored_sockets = [srvSocket]
    buffer = ''.encode('ascii')
    ft=0
    print ("Socket thread started (1)")
    while True:
        ready_to_read_sockets = select.select(
                monitored_sockets,
                tuple(),
                tuple()
            )[0]
        for ready_socket in ready_to_read_sockets:
                if ready_socket == srvSocket:
                    # If server socket is readable, accept new client
                    # connection.
                    client_socket, client_address = srvSocket.accept()
                    monitored_sockets.append(client_socket)
                    # Print connection received to terminal
                    print("Got a connection from %s to %s at %s" % (str(client_address),socket_port,str(datetime.now())))
                    # Connect to Log server
                    logHandlingCon(str(datetime.now()),str(client_address),socket_port, site,apikey)
                    #Send welcome message
                    client_socket.sendto(motd.encode('ascii'),client_address)
                    client_socket.sendto('\r\nPassword: '.encode('ascii'),client_address)
                    if ft <= 0:
                        ft=1

                else:
                    try:
                        message = ready_socket.recv(socket_buff_max)
                        if message:
                            # Client send correct message. Echo it. b'\r\n'
                            # Buffer the message untill newline is received
                            buffer += message
                            if buffer.endswith(b'\r\n'):
                                # Send message to client
                                if ft == 1:
                                    ready_socket.sendall('Login successful!'.encode('ascii'))
                                    ft = 2
                                # Print received messages to terminal
                                try:
                                    buffer.decode('ascii')
                                except:
                                    buffer = ('%s' % (buffer)).encode('ascii')
                                print(ready_socket.getpeername(),' : wrote : ', buffer.decode('ascii'))
                                logHandlingInput(str(datetime.now()),ready_socket.getpeername(),socket_port, buffer.decode('ascii'), site,apikey)
                                buffer = ''.encode('ascii')
                                # Send another message to client
                                ready_socket.sendall('\r\n#>: '.encode('ascii'))
                        else:
                            # Client connection is lost. Handle it.
                            monitored_sockets.remove(ready_socket)
                    except:
                        #Client lost. Handle it.
                        print ("Error: Client went away! ", ready_socket.getpeername())
                        monitored_sockets.remove(ready_socket)

#Write log to server first connection
def logHandlingCon(time, ip, port,site,apikey):
    #pf = ('Time: %s Hacker: %s On port: %s' % (time , ip, port)).encode('ascii')
    pf = urllib.parse.urlencode({'time' : time,
                         'ip'  : ip,
                         'port'    : port,
                         'apikey'    : apikey})
    urllib.request.urlopen(site, pf.encode('ascii'))

#Write log to server all input
def logHandlingInput(time, ip, port, usrinput, site,apikey):
    pf = urllib.parse.urlencode({'time' : time,
                         'ip'  : ip,
                         'port'    : port,
                         'input'   : usrinput,
                         'apikey'  : apikey})
    urllib.request.urlopen(site, pf.encode('ascii'))

#Start server thread
def runSocketServ(socket_family, socket_type, socket_port, socket_host, socket_max, socket_buff_max,motd,mp,site,apikey):
    try:
        if mp == 1:
            print('There are ',len(socket_port)," Ports!")
            for index in range(len(socket_port)):
               _thread.start_new_thread( crSocketServ, (socket_family, socket_type, int(socket_port[index]), socket_host, socket_max, socket_buff_max,motd,site,apikey) )
               print(index,": port ",socket_port[index], " started!")
        else:
               _thread.start_new_thread( crSocketServ, (socket_family, socket_type, socket_port, socket_host, socket_max, socket_buff_max,motd,site,apikey) )

        print ("Socket thread starting...(0)")
    except:
       print ("Error: unable to start Socket thread")
       
    while 1:
       pass
    

