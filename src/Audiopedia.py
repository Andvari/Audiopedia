'''
Created on 25.04.2012

@author: Nemo
'''

import urllib, urllib2, re

"""
log = open("audiopedia.txt", "w")
url = "http://server.audiopedia.su:8888/getmp3parms.php?mp3id="
val = 1000
while val<20500:
    link = url + str(val)
    print str(val) + " " + link
    request = urllib.urlopen(link)
    page = request.read()
    if len(page)>3:
        log.write("id" + str(val) + " ")
        log.write(page)
        log.write("\n")
    val+=1
"""

file = open("audiopedia.txt", "r")

page = file.read()

names = re.compile("<fname>(.*?)</fname>").findall(page)
dirs  = re.compile("<dir>(.*?)</dir>").findall(page) 


i = 0
while i<len(names)/1200:
    j = 0
    script_name = "rtmp" + str(i) + ".sh"
    script = open(script_name, "w");
    script.write("#!/bin/sh\n")
    while j < 1200:
        script.write('rtmpdump -r "http://server.audiopedia.su/vod" -y "mp3:')
        script.write(dirs[ i * 1200 + j ])
        script.write("/")
        script.write(names[ i * 1200 +j ])
        script.write('" -o "')
        script.write(names[ i * 1200 +j ])
        script.write('.flv" -q\n')
        j+=1
    script.close()
    i+=1
    
