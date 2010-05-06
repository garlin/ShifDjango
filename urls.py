from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('myproject.shifd_api.views',
	# Example:
	# (r'^myproject/', include('myproject.foo.urls')),

	(r'^get/(?P<sid>\w+)/(?P<format>(json|xml|php))$', 'get'),
	(r'^get/(?P<sid>\w+)$', 'get'),
	(r'^get/$', 'get'),

	(r'^getList/(?P<type_id>[1-3])/(?P<state>[0-1])/(?P<format>(json|xml|php))$', 'getList'),
	(r'^getList/(?P<type_id>[1-3])/(?P<state>[0-1])$', 'getList'),
	(r'^getList/(?P<type_id>[1-3])$', 'getList'),
	(r'^getList/$', 'getList'),
	(r'^getList$', 'getList'),

	(r'^getStats/(?P<sid>\w+)/(?P<format>\w+)$', 'getStats'),
	(r'^getStats/(?P<sid>\w+)$', 'getStats'),
	(r'^getStats/$', 'getStats'),

	(r'^search/(?P<keywords>\w+)/(?P<type_id>[1-3])/(?P<state>[0-1])/(?P<format>(json|xml|php))$', 'search'),
	(r'^search/(?P<keywords>\w+)/(?P<type_id>[1-3])$', 'search'),
	(r'^search/(?P<keywords>\w+)$', 'search'),
	(r'^search/$', 'search'),

	(r'^add/(?P<content>\w+)/(?P<type_id>[1-3])/(?P<tag>\w+)/(?P<privacy>(public|private))/(?P<format>(json|xml|php))$', 'add'),
	(r'^add/(?P<content>\w+)/(?P<type_id>[1-3])/(?P<tag>\w+)/(?P<privacy>(public|private))$', 'add'),
	(r'^add/(?P<content>\w+)/(?P<type_id>[1-3])/(?P<tag>\w+)$', 'add'),
	(r'^add/(?P<content>\w+)/(?P<type_id>[1-3])$', 'add'),
	(r'^add/(?P<content>\w+)$', 'add'),
	(r'^add/$', 'add'),

	(r'^edit/(?P<sid>\w+)/(?P<content>\w+)/(?P<type_id>[1-3])/(?P<tag>\w+)/(?P<privacy>(public|private))/(?P<format>(json|xml|php))$', 'edit'),
	(r'^edit/(?P<sid>\w+)/(?P<content>\w+)/(?P<type_id>[1-3])/(?P<tag>\w+)/(?P<privacy>(public|private))$', 'edit'),
	(r'^edit/(?P<sid>\w+)/(?P<content>\w+)/(?P<type_id>[1-3])/(?P<tag>\w+)$', 'edit'),
	(r'^edit/(?P<sid>\w+)/(?P<content>\w+)/(?P<type_id>[1-3])$', 'edit'),
	(r'^edit/(?P<sid>\w+)/(?P<content>\w+)$', 'edit'),
	(r'^edit/(?P<sid>\w+)$', 'edit'),
	(r'^edit/$', 'edit'),

	(r'^delete/(?P<sid>\w+)/(?P<format>\w+)$', 'delete'),
	(r'^delete/(?P<sid>\w+)$', 'delete'),
	(r'^delete/$', 'delete'),

	(r'^archive/(?P<sid>\w+)/(?P<state>(1))/(?P<format>(json|xml|php))$', 'archive'),
	(r'^archive/(?P<sid>\w+)$', 'archive'),
	(r'^archive/$', 'archive'),

	(r'^unarchive/(?P<sid>\w+)/(?P<state>(0))/(?P<format>(json|xml|php))$', 'archive'),
	(r'^unarchive/(?P<sid>\w+)$', 'archive'),
	(r'^unarchive/$', 'archive'),

	(r'^getExtraInfo/(?P<content>\w+)/(?P<format>(json|xml|php))$', 'getExtraInfo'),
	(r'^getExtraInfo/(?P<content>\w+)$', 'getExtraInfo'),
	(r'^getExtraInfo$', 'getExtraInfo'),

	(r'^callback/$','callback'),

	# Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
	# to INSTALLED_APPS to enable admin documentation:
	# (r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# Uncomment the next line to enable the admin:
	# (r'^admin/', include(admin.site.urls)),
)