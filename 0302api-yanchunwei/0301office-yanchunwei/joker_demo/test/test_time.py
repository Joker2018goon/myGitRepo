import time
import subprocess
from datetime import datetime
from dateutil import parser
# now=time.strftime('%X',time.localtime())

# print(now)
# print(now[12:16])

# d='8:10'.rjust(5,'0')
# print(d)

# # for i in range(1,1000):
# #     i=str(i).rjust(4,'0')
# #     print(i)
# #     time.sleep(1)
# str='闹钟响啦，起床啦!'
# print(str)

# m=subprocess.Popen(['start','起床歌.mp3'],shell=True)
# for i in range(5):
#     # print(str(i)+'\r',end='',flush=True)
#     print(i)
#     time.sleep(1)

# pid=m.pid
# print(pid)
# # kill_command = f'taskkill /pid {pid} -t -f'
# # subprocess.Popen(kill_command ,shell=True)

# m.terminate()
# # m.kill()


# '2018/1/8 14:28'
# 中文的年月日的处理 ， 如'2018年2月8日 14:28'
# 只有日期，自动追加时间，如  1.7 或者 1月7日 
# 直接写时间的，默认是今天


y=datetime.now()
print(y)
print(str(y)[:4])

d='2月8日 14:28'
d.replace('年','-')
print(d.replace('年','-'))
d.replace('月','-')
print(d.replace('年','-').replace('月','-'))
d.replace('日','')
print(d.replace('年','-').replace('月','-').replace('日',''))


now=time.strftime('%Y-%m-%d %X',time.localtime())
print(type(now))
print(now)

print('===========')

d=int('06')
print(type(d))
print('===========')

if '1':
    print('222222')

print('比较时间戳')
print(time.time())
# '2013-05-13 03:22:11'
now1=time.time()
dt = "2013-05-13 03:22:11"

#转换成时间数组
timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
#转换成时间戳
timestamp = time.mktime(timeArray)

print(timestamp)
print(type(timestamp))
print(type(now1))
if timestamp>=now1:
    print('备忘未来的时间')
else:
    print('请输入不小于当前时间的日期')



if int('02') in range(1,13):
    print('*********************12222****')