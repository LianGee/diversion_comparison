# -*- coding: utf-8 -*-
import dpkt
import os
import time
from protobuf.cs_pb2 import ReqBody, RespBody
import struct
from case.test_case import TestCase


class PcapService:
    def __init__(self, cappath):
        self.cappath = os.path.join(os.path.dirname(__file__) + '/' + cappath)

    def get_udp_data(self, step=100, r=0, f=None):
        print "read cap file :" + self.cappath
        pcap = dpkt.pcap.Reader(f)
        post_data = []
        start_time = int(time.time() * 1000)
        i = r*step
        for ts, buf in pcap:
            if i >= (r+1)*step:
                break
            try:
                eth = dpkt.ethernet.Ethernet(buf)
                ip = eth.data
                udp = ip.data
            except Exception, e:
                print Exception, ":", e
                continue
            try:
                test = TestCase()
                test.id = i
                test.data = udp.data
                test.seq = self.get_seq(test.data)
                test.request = self.get_request(test.data)
                post_data.append(test)
                i += 1
            except (dpkt.dpkt.NeedData, dpkt.dpkt.UnpackError):
                continue
        end_time = int(time.time() * 1000)
        print "cost time is:" + str(end_time - start_time) + "ms"
        return post_data

    @staticmethod
    def get_seq(udp_data):
        head = struct.unpack("!BcHQI4H", udp_data[0:24])
        return head[3]  # seq

    @staticmethod
    def get_response(udp_data):
        res = RespBody()
        new_data = udp_data[24:]
        if len(new_data) < 10240:
            res.ParseFromString(new_data)
        else:
            res = None
        return res

    @staticmethod
    def get_request(udp_data):
        req = ReqBody()
        new_data = udp_data[24:]
        if len(new_data) < 10240:
            req.ParseFromString(new_data)
        else:
            req = None
        return req




