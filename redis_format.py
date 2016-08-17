#coding=utf-8
'''
Created on 2016年8月17日

@FileName: redis_format.py

@Description: (描述) 

@Site:  http://www.sugarguo.com/

@author: 'Sugarguo'

@version V1.0.0

'''

import sys
sys.path.append("..")

import re
import time




aofstr = ""

aofList = []

tempList = []

parameterList = []

commandList = []


writefile = open("command.txt","w")


def getFileLine(filename):
    getFileList = []
    getFile = open(filename,"r")
    for item in getFile.readlines():
        m = re.match(r'\$(\w+)', item)
        n = re.match(r'\*(\w+)', item)
        if m or n:
            continue
        else:
            item = item.replace("\r\n","").replace("\n","")
            getFileList.append(item)
    getFile.close()
    return getFileList

def getFileContent(filename):
    getFileStr = ""
    getFile = open(filename,"r")
    getFileStr = getFile.read()
    getFile.close()
    return getFileStr

print "-_-==--||==============*_*====-_-"
print "Ready GO!\n"
print "Read file appendonly.aof! \n"

aofilename = "appendonly.aof"

print "-_-==--||==============*_*====-_-"
print "Now read file to str!\n"


aofstr = getFileContent(aofilename)

print "-_-==--||==============*_*====-_-"
print "OK!\nRead file to list!\n"

start = time.clock()
aofList = getFileLine(aofilename)
end = time.clock()
print "time use : %f s" % (end - start)

print "-_-==--||==============*_*====-_-"
print "OK!\nGet parameter list!\n"

start = time.clock()
parameterList = re.findall(r"\*(\w+)",aofstr)
end = time.clock()
print "time use : %f s" % (end - start)

print "OK!\n"

print "-_-==--||==============*_*====-_-"
print "Parameter has ",str(len(parameterList))," \n"

start = time.clock()
for index,length in enumerate(parameterList):
    if index % 1000 == 0:
        end = time.clock()
        print "time use : %f s" % (end - start)
        start = time.clock()
    length = int(length)
    tempList = []
    tempList = aofList[:length]
    commandList.append( " ".join(tempList) )
    del aofList[0:length]

end = time.clock()
print "time use : %f s" % (end - start)
print "-_-==--||==============*_*====-_-"
print "OK\nWrite file!\n" 

for item in commandList:
    writefile.write(item + "\r\n")

writefile.close()

print "-_-==--||==============*_*====-_-"
print "Everything Ok!\nEnjoy it!\n"

