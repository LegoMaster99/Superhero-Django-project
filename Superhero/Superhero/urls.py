
from django.conf.urls import url
from django.contrib import admin

from comments.views import homeView ,batmanView, supermanView, wonderWomanView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', homeView.as_view()),
    url(r'^batman/$', batmanView.as_view(), name='batman'),
    url(r'^superman/$', supermanView.as_view(), name='superman'),
    url(r'^wonderwoman/$', wonderWomanView.as_view(), name='wonderwoman'),
]
