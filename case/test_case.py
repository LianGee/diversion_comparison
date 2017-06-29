from protobuf.cs_pb2 import RespBody


test_time_out = []  # 2
err_code_99 = []  # 3
err_code_1 = []  # 4
online_time_out = []  # 5
err = []  # error bug!
success = []
failed = []


class TestCase:
    def __init__(self, id=0, data=None, seq=0, request=None, response1=None, response2=None):
        self.id = id
        self.data = data
        self.seq = seq
        self.request = request
        self.response1 = response1
        self.response2 = response2
        self.result = 0  # 0: error bug, 1 pass, 2 test time out, 3 error_code_99, 4 error_code_1, 5 online time out

    def check_response(self):
        if self.response2 in self.response1:
            success.append(self.id)
            self.result = 1
        elif 'err_code: 99' in self.response1 or 'flag: 99' in self.response1:
            err_code_99.append(self.id)
            failed.append(self.id)
            self.result = 3
        elif 'err_code: 1' in self.response1:
            err_code_1.append(self.id)
            failed.append(self.id)
            self.result = 4
        elif len(self.response1) == 0:
            test_time_out.append(self.id)
            failed.append(self.id)
            self.result = 2
        elif 'err_code: 99' in self.response2 or 'flag: 99' in self.response2\
                or len(self.response2 == 0):
            online_time_out.append(self.id)
            success.append(self.id)
            self.result = 5
        else:
            err.append(self.id)
            failed.append(self.id)
            self.result = 0

    @staticmethod
    def set_response(reply):
        res = RespBody()
        data = reply[24:]
        print 'response length:', len(data)
        try:
            res.ParseFromString(data)
        except Exception, e:
            res = ''
            print e, 'response decode failed!!!!'
        return str(res)

    @staticmethod
    def show_reslut():
        print 'failed %s' % len(failed), err
        print 'success %s' % len(success), success
        print 'test time out %s' % len(test_time_out), test_time_out
        print 'err_code_99 %s' % len(err_code_99), err_code_99
        print 'err_code_1 %s' % len(err_code_1), err_code_1
        print 'online time out %s' % len(online_time_out), online_time_out
        print 'err %s' % len(err), err

