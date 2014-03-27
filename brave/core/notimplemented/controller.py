# encoding: utf-8

from __future__ import unicode_literals

from web.core import Controller, HTTPMethod

log = __import__('logging').getLogger(__name__)

class Notimplemented(HTTPMethod):
	def get(self):
		return 'brave.core.template.notimplemented',dict()
class NotimplementedController(Controller):
	index = Notimplemented()
