from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^db', hello.views.db, name='db'),
    url(r'^compileasm', hello.views.compileasm, name='compileasm'),
    url(r'^runasm', hello.views.runasm, name='runasm'),
    url(r'^ts2wmv', hello.views.ts2wmv, name='ts2wmv'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^save', hello.views.save, name='save'),
]
