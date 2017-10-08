from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sendEmail/', hello.views.sendEmail, name='sendEmail'),
    url(r'^checkOut/', hello.views.checkOut, name='checkOut'),
    url(r'^checkOutPersist/', hello.views.checkOutPersist, name='checkOutPersist'),
]
