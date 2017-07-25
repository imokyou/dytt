# coding=utf8
from lib import utils
from dbmodel.models import Video


def home(req):
    data = {'records': {}}
    records = Video.objects.order_by('section').order_by('-pubdate').all()
    for r in records:
        i = 0
        if r.section not in data['records']:
            data['records'][r.section] = []
        if len(data['records'][r.section]) < 15:
            data['records'][r.section].append(r)
    return utils.TRender(req, 'index.html', data)
