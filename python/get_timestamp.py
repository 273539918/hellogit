#!/usr/bin/python
# -*- coding: UTF-8 -*-
## 给出指定日期的开始时间戳和结束时间戳

def get_timestamp(type1, type2, days):
    # type: (str, str, int) -> object
    """
    给出指定日期的开始时间戳和结束时间戳
    :param type1: before or future.  before今天之前，future今天之后
    :param type2: start or end . 开始时间或结束时间的时间戳
    :param days: 天数
    :return: timestamp
    """
    today = datetime.date.today()

    if type1 == 'before':
        target_day = today - datetime.timedelta(days=days)
    else:
        target_day = today + datetime.timedelta(days=days)

    if type2 == 'start':
        return int(time.mktime(time.strptime(str(target_day), '%Y-%m-%d'))) * 1000
    else:
        target_day += datetime.timedelta(days=1)
        return int(time.mktime(time.strptime(str(target_day), '%Y-%m-%d'))) * 1000 - 1