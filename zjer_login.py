#*****************************************************************************************
# this is daily basis login function for zhuzhu's zjer requirement
#
# Version: 0.1
# Auther: Allan DENG
# Date : 2018-04-15
#*****************************************************************************************


import urllib3
print 'zjer auto operation script'
pool = urllib3.PoolManager()
response = pool.request('GET', 'http://yun.zjer.cn')

if response.status == 200:
    print 'zjer is available status: 200'
else:
    print 'zjer is not available right now, will try later'
    exit(0)

print 'start to login'
print response.data
