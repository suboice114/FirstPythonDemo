#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2019/9/13 14:35
# @Author  : su
# @File    : use-datetime.py
"""
datetime模块: Python内置处理时间和日期的标准库

datetime模块还包含一个datetime类，通过from datetime import datetime导入的才是datetime这个类。
"""
from datetime import datetime, timedelta, timezone

# 获取当前datetime
now = datetime.now()
print('now =', now)
print('type(now) =', type(now))

# 用指定日期时间创建datetime
dt = datetime(2019, 9, 13, 14, 38)
print(dt)

# 把datetime转换为timestamp (timestamp是一个浮点数。如果有小数位，小数位表示毫秒数。)
time_stamp = dt.timestamp()
print(time_stamp)

# timestamp转换为 本地 datetime
t = datetime.fromtimestamp(time_stamp)
print(t)

# timestamp转换为 UTC+0 的datetime
t1 = datetime.utcfromtimestamp(time_stamp)
print(t1)

# str转换为datetime
cDay = datetime.strptime('2019-9-13 14:44:52', '%Y-%m-%d %H:%M:%S')
print(cDay)

# datetime转换为str
print(now.strftime('%a, %b %d %H:%M'))

# 对日期进行加减:
print('current datetime =', cDay)
print('current + 10 hours =', cDay + timedelta(hours=10))
print('current - 1 day =', cDay - timedelta(days=1))
print('current + 2.5 days =', cDay + timedelta(days=2, hours=12))

# 把时间从UTC+0时区转换为UTC+8:
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print('UTC+0:00 now =', utc_dt)

utc8_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print('UTC+8:00 Beijing now =', utc8_dt)

utc9_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print('UTC+9:00 Tokyo now =', utc9_dt)
