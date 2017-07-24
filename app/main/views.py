# coding=utf8
from lib import utils


def home(req):
	data = {}
	return utils.TRender(req, 'index.html', data)
