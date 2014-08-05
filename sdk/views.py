#! /usr/bin/env python
# coding=utf-8

from django.http import HttpResponse
from django.shortcuts import render_to_response
from forms import YeahTestForm
from sdk.models import LogParser
import os
import urllib
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

    yeahmobi_offline = 'http://172.20.0.69:8080/realquery/report?'
    yeahmobi_online = 'http://resin-yeahmobi-214401877.us-east-1.elb.amazonaws.com:18080/report/report?'
    trading_online = 'http://resin-track-1705388256.us-east-1.elb.amazonaws.com:18080/report/report?'

    if method == 'yeahmobi_offline':
        url = yeahmobi_offline
    elif method == 'yeahmobi_online':
        url = yeahmobi_online
    else:
        url = trading_online

    postdata = urllib.urlencode({'report_param': receive})

    rsp = urllib2.build_opener().open(urllib2.Request(url, postdata)).read()

    try:
        rspdata = json.loads(rsp)['data']['data']
    except KeyError, e:
        return HttpResponse('No Data Found')
    else:
        pass
    num = len(rspdata) - 1
    return render_to_response('result.html', {'num':num, 'request_data':rspdata})

def index(request):
    return render_to_response('index.html')

def logparser(request):
    if request.method == "POST":
        ytf = YeahTestForm(request.POST,request.FILES)
        if ytf.is_valid():
            #获取表单信息
            keywords = ytf.cleaned_data['keywords']
            filepath = ytf.cleaned_data['filepath']
            #写入数据库
            lp = LogParser()
            lp.keywords = keywords
            lp.filepath = filepath
            lp.save()
            return HttpResponse('upload ok!')
    else:
        ytf = YeahTestForm()
    return render_to_response('upload.html',{'ytf':ytf})