#! /usr/bin/env python
# coding=utf-8

from django.http import HttpResponse
from django.shortcuts import render_to_response
from forms import YeahTestForm
from sdk.models import LogParser
import os
import urllib
import time
import json
import  urllib2
# Create your views here.


def dencrypt(request):

    postdata = request.POST
    if postdata.get('param', None) is None or postdata.get('key', None) is None:
        return render_to_response('main.html', {'output': '',
                                                'input': '',
                                                'key': ''})
    try:
        param, key, methodtype = postdata['param'], postdata['key'], postdata['methodtype']
    except KeyError, e:
        return render_to_response('main.html', {'output': 'get postdata error'})
    try:
        jarcmd = 'java -Xbootclasspath/a:externlib/3DES.jar:externlib/commons-codec-1.9.jar: -jar externlib/parser.jar "%s" "%s" "%s"' % (methodtype, param, key)
        output = os.popen(jarcmd).read()
        if output == '':
            return render_to_response('main.html', {'output': 'decode input error'})
    except Exception:
        return render_to_response('main.html', {'output': 'execute method error'})
    return render_to_response('main.html', {'output': output,
                                            'input': param,
                                            'key': key})

def show_report(request):
    return render_to_response('sendreq.html')

def get_report_data(request):
    receive = request.POST.get('settings', 'no value')
    method = request.POST.get('methodtype')

    try:
        test = json.dumps(receive)
    except ValueError:
        return HttpResponse('settings is not json')

    druid_offline = 'http://172.20.0.69:8080/realquery/report?'
    druid_online = 'http://resin-yeahmobi-214401877.us-east-1.elb.amazonaws.com:18080/report/report?'
    mysql_online = 'http://report.yeahmobi.com/report?'
    trading_online = 'http://resin-track-1705388256.us-east-1.elb.amazonaws.com:18080/report/report?'
    trading_offline = 'http://172.20.0.70:8080/track/report?'

    if method == 'druid_offline':
        url = druid_offline
    elif method == 'druid_online':
        url = druid_online
    elif method == 'mysql_online':
        url = mysql_online
    elif method == 'trading_online':
        url = trading_online
    else:
        url = trading_offline

    postdata = urllib.urlencode({'report_param': receive})

    begin = time.time()
    rsp = urllib2.build_opener().open(urllib2.Request(url, postdata)).read()
    spend = time.time() - begin

    try:
        rspdata = json.loads(rsp)['data']['data']
    except KeyError, e:
        return HttpResponse(rsp)
    else:
        pass
    num = len(rspdata) - 1
    return render_to_response('result.html', {'num':num, 'spend':spend ,'request_data':rspdata})

def index(request):
    return render_to_response('index.html')

def login(request):
    return render_to_response('login.html')

def autoreport(request):
    return render_to_response('autoreport.html')
