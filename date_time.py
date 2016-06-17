#日期时间模块
from datetime import datetime, timedelta, timezone
now = datetime.now()
print(now)

dt = datetime(2016, 6, 16, 16, 20, 25)
print(dt)

print(now.timestamp())

#转换为字符串
print(now.strftime('%a, %b %d %H:%M'))

dt1 = datetime.strptime('2016-6-16 16:20:58', '%Y-%m-%d %H:%M:%S')
print(dt1)

dt1 = dt1 + timedelta(days = 1)
print(dt1)

dt1 = dt1 + timedelta(hours = 10)
print(dt1)

#时区转换
#UTC时间
utc_dt = datetime.utcnow().replace(tzinfo = timezone.utc)
print(utc_dt)

#北京时间
bj_dt = utc_dt.astimezone(timezone(timedelta(hours = 8)))
print(bj_dt)

#东京时间
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours = 9)))
print(tokyo_dt)

import dateutil.parser
print(dateutil.parser.parse('2015-6-1 08:10:30+07:00'))
print(dateutil.parser.parse('2015-6-1 08:10:30+07:00').timestamp())

t = 1433121030.0
print(datetime.fromtimestamp(t))

