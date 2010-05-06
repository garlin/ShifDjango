# Create your views here.
import urllib, urllib2
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.core.urlresolvers import reverse

user = ''
password = ''

def get(request, sid='', format='json'):
	try:
		content = request.REQUEST['sid']
	except:
		pass
	
	base_url = 'http://shifd.com/api/v1/get?' # API URL (source: http://shifd.com/developers/v1/get)
	params = {'sid' : sid, 'format' : format}
	requesturl = base_url + "&".join(["%s=%s" % (k, v) for k, v in params.items()])
	fullrequesturl = addBasicAuthStringToUrl(requesturl, user, password)
	response = urllib2.urlopen(fullrequesturl)
	return HttpResponse(response)

def getList(request, type_id='1', state='0', format='json'):
	try:
		type_id = request.REQUEST['type_id']
	except:
		pass

	base_url = 'http://shifd.com/api/v1/getList?' # API URL (source: http://shifd.com/developers/v1/getList)
	params = {'type_id' : type_id, 'state' : state, 'format' : format}
	requesturl = base_url + "&".join(["%s=%s" % (k, v) for k, v in params.items()])
	fullrequesturl = addBasicAuthStringToUrl(requesturl, user, password)
	response = urllib2.urlopen(fullrequesturl)
	return HttpResponse(response)

def getStats(request, sid='', format='json'):
	try:
		content = request.REQUEST['sid']
	except:
		pass
	
	base_url = 'http://shifd.com/api/v1/getStats?' # API URL (source: http://shifd.com/developers/v1/getStats)
	params = {'sid' : sid, 'format' : format}
	requesturl = base_url + "&".join(["%s=%s" % (k, v) for k, v in params.items()])
	fullrequesturl = addBasicAuthStringToUrl(requesturl, user, password)
	response = urllib2.urlopen(fullrequesturl)
	return HttpResponse(response)

def search(request, keywords, type_id='1', state='0', format='json'):
	try:
		content = request.REQUEST['keywords']
	except:
		pass
	
	try:
		type_id = request.REQUEST['type_id']
	except:
		pass
	
	base_url = 'http://shifd.com/api/v1/search?' # API URL (source: http://shifd.com/developers/v1/search)
	params = {'keywords' : urllib.quote(keywords), 'type_id' : type_id, 'state' : state, 'format' : format}
	requesturl = base_url + "&".join(["%s=%s" % (k, v) for k, v in params.items()])
	fullrequesturl = addBasicAuthStringToUrl(requesturl, user, password)
	response = urllib2.urlopen(fullrequesturl)
	return HttpResponse(response)

def add(request, content='', type_id='1', tag='', privacy='public', format='json'):
	try:
		content = request.REQUEST['content']
	except:
		pass
	
	try:
		type_id = request.REQUEST['type_id']
	except:
		pass
	
	base_url = 'http://shifd.com/api/v1/add?' # API URL (source: http://shifd.com/developers/v1/add)
	params = {'content' : urllib.quote(content), 'type_id' : type_id, 'tag' : urllib.quote(tag), 'privacy' : privacy, 'format' : format}
	requesturl = base_url + "&".join(["%s=%s" % (k, v) for k, v in params.items()])
	fullrequesturl = addBasicAuthStringToUrl(requesturl, user, password)
	response = urllib2.urlopen(fullrequesturl)
	return HttpResponse(response)

def edit(request, sid='', content='', type_id='1', tag='', privacy='public', format='json'):
	try:
		content = request.REQUEST['content']
	except:
		pass
	
	try:
		type_id = request.REQUEST['type_id']
	except:
		pass
	
	try:
		content = request.REQUEST['sid']
	except:
		pass
	
	base_url = 'http://shifd.com/api/v1/edit?' # API URL (source: http://shifd.com/developers/v1/edit)
	params = {'sid' : sid, 'type_id' : type_id, 'content' : urllib.quote(content), 'tag' : urllib.quote(tag), 'privacy' : privacy, 'format' : format}
	requesturl = base_url + "&".join(["%s=%s" % (k, v) for k, v in params.items()])
	fullrequesturl = addBasicAuthStringToUrl(requesturl, user, password)
	response = urllib2.urlopen(fullrequesturl)
	return HttpResponse(response)

def delete(request, sid='', format='json'):
	try:
		content = request.REQUEST['sid']
	except:
		pass
	
	base_url = 'http://shifd.com/api/v1/delete?' # API URL (source: http://shifd.com/developers/v1/delete)
	params = {'sid' : sid, 'format' : format}
	requesturl = base_url + "&".join(["%s=%s" % (k, v) for k, v in params.items()])
	fullrequesturl = addBasicAuthStringToUrl(requesturl, user, password)
	response = urllib2.urlopen(fullrequesturl)
	return HttpResponse(response)

def archive(request, sid='', state='1', format='json'):
	try:
		content = request.REQUEST['sid']
	except:
		pass
	
	base_url = 'http://shifd.com/api/v1/archive?' # API URL (source: http://shifd.com/developers/v1/archive)
	params = {'sid' : sid, 'state' : state, 'format' : format}
	requesturl = base_url + "&".join(["%s=%s" % (k, v) for k, v in params.items()])
	fullrequesturl = addBasicAuthStringToUrl(requesturl, user, password)
	response = urllib2.urlopen(fullrequesturl)
	return HttpResponse(response)

def unarchive(request, sid='', state='0', format='json'):
	try:
		content = request.REQUEST['sid']
	except:
		pass
	
	base_url = 'http://shifd.com/api/v1/archive?' # API URL (source: http://shifd.com/developers/v1/archive)
	params = {'sid' : sid, 'state' : state, 'format' : format}
	requesturl = base_url + "&".join(["%s=%s" % (k, v) for k, v in params.items()])
	fullrequesturl = addBasicAuthStringToUrl(requesturl, user, password)
	response = urllib2.urlopen(fullrequesturl)
	return HttpResponse(response)

def getExtraInfo(request, content='', format='json'):
	try:
		content = request.REQUEST['content']
	except:
		pass
	
	base_url = 'http://shifd.com/api/v1/getExtraInfo?' # API URL (source: http://shifd.com/developers/v1/getExtraInfo)
	params = {'content' : urllib.quote(content), 'format' : format}
	requesturl = base_url + "&".join(["%s=%s" % (k, v) for k, v in params.items()])
	fullrequesturl = addBasicAuthStringToUrl(requesturl, user, password)
	response = urllib2.urlopen(fullrequesturl)
	return HttpResponse(response)

def callback(request, username='garlin', tag='', content='test', date_created='', sid='qB2Z', type='1'):
	return HttpResponseRedirect(reverse('myproject.shifd_api.views.get',args=(sid,)))

def addBasicAuthStringToUrl(in_url, u, p):
	# Append usename & password to query string
	params = {'username' : u, 'password' : p}
	fullrequesturl = in_url + '&' + "&".join(["%s=%s" % (k, v) for k, v in params.items()])
	return (fullrequesturl)

def parseShifDXml(in_xml):
	return (data)

def parseShifDJson(in_json):
	return (data)