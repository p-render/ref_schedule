from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'refwatch.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'refs.views.Index', name='index'),
    url(r'^register/$', 'refs.views.RefRegistration'),
    url(r'^login/$', 'refs.views.LoginRequest'),
    url(r'^logout/$', 'refs.views.LogoutRequest'),
    url(r'^profile/$', 'refs.views.Profile'),
    url(r'^delete_user/$', 'refs.views.DeleteUser'),
#    url(r'^resetpassword/passwordsent/$', 'django.contrib.auth.views.password_reset_done'),
#    url(r'^resetpassword/$', 'django.contrib.auth.views.password_reset'),
#    url(r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm'),
#    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete'),
)
