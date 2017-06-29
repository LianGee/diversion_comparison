from socket_client.server import Server
from case.test import create_test_case
from socket_client.send_request import run
from case.test_case import TestCase
import threading
import time
from config import __Config


class Param:
    def __init__(self, step, r, name):
        self.step = step
        self.r = r
        self.file = name
        self.f = open(name, 'r')


def test_thread(param):
    tests = create_test_case(param.file, param.step, param.r, param.f)
    t1 = threading.Thread(target=run, args=(tests, test, 1))
    t2 = threading.Thread(target=run, args=(tests, online, 2))
    t1.setDaemon(True)
    t2.setDaemon(True)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    for tc in tests:
        tc.check_response()
    TestCase.show_reslut()

if __name__ == '__main__':
    config = __Config()
    test = Server(config.test_ip, config.test_port)
    online = Server(config.online_ip, config.online_port)
    start = int(time.time() * 1000)
    params = []

    if type(config.file) is list:
        for i in range(len(config.file)):
            para = Param(config.step, i, config.file[i])
            params.append(para)
    else:
        params.append(Param(config.step, config.r, config.file))
    if len(params) > 1:
        for i in range(len(params)):
            t = threading.Thread(target=test_thread(), args=(params[i]))
            t.setDaemon(True)
            t.start()
            t.join()
    else:
        test_thread(params[0])
    end = int(time.time() * 1000)
    print str(end - start) + "ms"

