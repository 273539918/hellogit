#!/usr/bin/python
# -*- coding: UTF-8 -*-
## 用来对某一个url 做压力测试，得到请求的平均耗时

import json
import requests
import logging


cost_time = []

class Worker():


    def __init__(self,num,url,params):
        self.num = num
        self.url = url
        self.params = params

    def send_request(self):


        try:
            r =requests.get(self.url,params=self.params,timeout=30)
            return r
        except Exception as e:
            print(e)



    def circulation(self):

        for i in range(self.num):
            r = Worker.send_request()
            if r:
                cost_time.append(r.elapsed.total_seconds())

    def output_result(self):


        print("request total num: %s" % self.num)
        print("request success num: %s" % len(cost_time))
        print("max request time: %s" % max(cost_time))
        print("min request time: %s" % min(cost_time))
        print("total request time: %s" % sum(cost_time))
        print("avg request time: %s" % (sum(cost_time) / self.num) )


if __name__ == '__main__':


    url = "http://www.baidu.com"
    Worker = Worker(2,url,{})
    Worker.circulation()
    Worker.output_result()


