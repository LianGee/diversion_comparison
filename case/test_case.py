test_time_out = []  # 2
err_code_99 = []  # 3
err_code_1 = []  # 4
online_time_out = []  # 5
err = []  # error bug!
success = []
failed = []


class TestCase:
    def __init__(self, id=0, seq=0, request=None, response1=None, response2=None):
        self.id = id
        self.seq = seq
        self.request = request
        self.response1 = response1
        self.response2 = response2
        self.result = 0  # 0: error bug, 1 pass, 2 test time out, 3 error_code_99, 4 error_code_1, 5 online time out

    def check_response(self):
        if 'err_code: 99' in self.response1 or 'flag: 99' in self.response1:
            test_time_out.append(self.id)
            failed.append(self.id)
        elif 'err_code: 1' in self.response1:
            err_code_1.append(self.id)
            failed.append(self.id)
        elif 'err_code: 99' in self.response2 or 'flag: 99' in self.response2\
                or len(self.response2 == 0):
            online_time_out.append(self.id)
            success.append(self.id)
        else:
            err.append(self.id)
            failed.append(self.id)
