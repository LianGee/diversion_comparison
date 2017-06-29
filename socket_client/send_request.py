import socket
from cap.parse_cap import PcapService
import time
import sys
import threading


def connect(serv):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(0.1)
    except socket.error, msg:
        print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
        sys.exit()
    try:
        remote_ip = socket.gethostbyname(serv.host)
    except socket.gaierror:
        # could not resolve
        print 'Hostname could not be resolved. Exiting'
        sys.exit()
    print 'Ip address is ' + serv.host
    s.connect((serv.host, serv.port))
    print 'Socket Connected to ' + serv.host + ' on ip ' + remote_ip
    return s


def send_request(serv, test_case, s):
    try:
        print 'request %s is:\n' % test_case.id, test_case.request
        print 'id: %s seq: %s' % (test_case.id, test_case.seq)
        print 'to' + serv.host + ':' + str(serv.port)
        s.sendall(test_case.data)
        print 'request %s send successfully' % test_case.id
    except socket.error:
        print 'send failed=================='
        sys.exit()


def recv_response(serv, tc, type, s):
    try:
        start = int(time.time() * 1000)
        reply = s.recv(10240)
        end = int(time.time() * 1000)
        cost = end - start
        if tc.seq != PcapService.get_seq(reply):
            print 'seq is not correct'
        else:
            print 'recieve success!'
            if type == 1:
                if cost >= 100:
                    tc.response1 = ''
                    print 'cost >= 100 ms'
                else:
                    tc.response1 = tc.set_response(reply)
                print 'response1 %s ' % tc.id, tc.response1
            elif type == 2:
                if cost >= 100:
                    tc.response2 = ''
                else:
                    tc.response2 = tc.set_response(reply)
                print 'response2 %s ' % tc.id, tc.response2
    except socket.timeout:
        if type == 1:
            tc.response1 = ''
        if type == 2:
            tc.response2 = ''
        print 'socket time out'


def run(tc, serv, type):
    mutex = threading.Lock()
    s = connect(serv)
    for t in tc:
        mutex.acquire()
        send_request(serv, t, s)
        recv_response(serv, t, type, s)
        mutex.release()
    s.close()
