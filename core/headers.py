# -*- coding: utf-8 -*-
# Author :  #Bitwis3 - Hamid Mahmoud -

from concurrent import futures
from core.colors import *
from core.usage import *
import requests
import sys


headList = []
gsite = ""
gpayload = ""
progList = 0
#Progress Bar
def progress(count, total, status=''):
    bar_len = 1
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '!', status))
    sys.stdout.flush()


# Single Injection
def InjectHead(headVar):

    global gpayload
    global gsite
    global progList
    global args

    m = args.mobile
    test = str(gsite)
    hdr = {str(headVar).rstrip():str(gpayload)}

    try:
        response = requests.get(str(test).rstrip(), headers=hdr,timeout=3)
        res_headers = response.headers
        progList += 1
        if str(headVar).rstrip() in response.headers:
            if response.headers[str(headVar).rstrip()] == gpayload :
                print(Y+'['+R+'+'+Y+'] Target: '+str(test).rstrip()+' is '+R+'Vulnerable'+Y+' to Header Injection ['+R+str(headVar).rstrip()+Y+']'+G)
        else:
            if m == False:
                progress(progList,1000,'Header Injection Progress')
            if m == True:
                print(Y+'['+R+'+'+Y+'] Target: '+str(test).rstrip()+' is'+B+' not'+Y+' Vulnerable to Header Injection ['+R+str(headVar).rstrip()+Y+']'+G)

    except requests.Timeout as err:
        pass


# Check Header Injection with a given Payload
def HeadInjection(site,payload,worker_threads):
    global gsite,gpayload
    gsite = site
    gpayload = payload
    f = open('core/headers.txt','r')
    countIter = 0
    try:
        headList = f.readlines()
    except:
        pass
    finally:
        f.close()
        if len(headList) > 0:
            workers = min(int(worker_threads),len(headList))
            with futures.ThreadPoolExecutor(workers) as executor:
                res = executor.map(InjectHead,headList)


