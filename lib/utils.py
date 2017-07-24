# coding=utf-8
import json
from django.http import HttpResponse
from django.shortcuts import render


def HttpJSONResponse(js):
    return HttpResponse(json.dumps(js),
                        content_type='application/json')


def NormalResp(d={}):
    return HttpResponse(json.dumps({'c': 0, 'd': d}),
                        content_type='application/json')



def TRender(request, template_file, data):
    return render(request, template_file, data)