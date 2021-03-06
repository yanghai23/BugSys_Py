#/usr/bin/python
# _*_ coding: UTF-8 _*_
import time
import datetime
import os


#timer(10)

def pullErrFile(time,packageName,fileName):
    line = "aws s3 sync s3://sdk-crash-1/%s/%s   %s"%(time,packageName,fileName)
    print(line)
    os.system(line)


def generateFileName(packagename,time):
    return "%s__%s"%(packagename,time)

def generateTime():
    last_date = datetime.date.today()
    return last_date.strftime("%Y-%-m-%-d")
#print(generateFileName("test"))

def pullFile(day):
    packages = set(['com.wifi.cool','photo.studio.editor.selfie.camera','com.yiba.baidu.wifi','com.xvideostudio.videoeditorlite','com.necta.wifimousefree','com.infreewifi.cct','com.dianxinos.dxbs','com.yiba.sdk', 'com.yiba.sharewe.lite.activity', 'com.baidu.app', 'com.yiba.baidu.wifi'])
    for name in packages:
        print("name = %s"%name)
        pullErrFile(generateTime(),name,generateFileName(name,generateTime()))
        #pullErrFile(day,name,generateFileName(name,day))


def read_config():
    try:
        path = "appNames.txt"

        iter_f = iter(open(path))
        for line in iter_f:
            print("name = %s"%line)
            name = line.strip('\n')
            pullErrFile(generateTime(),name,generateFileName(name,generateTime()))
            print(line)
    except Exception as e:
        print("has an exception= %s"%e)

