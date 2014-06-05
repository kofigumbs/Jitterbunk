from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from jitterbunk_app.models import Bunk, UserProfile

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$',
        ListView.as_view(
            queryset=Bunk.objects.order_by('-time')[:25],
            context_object_name='latest_bunk_list',
            template_name='index.html')),

    url(r'^(?P<pk>\d+)/?$', 'jitterbunk_app.views.profile'),
    url(r'^(?P<pk>\d+)/bunk/?$',
        DetailView.as_view(
            model=UserProfile,
            template_name='bunk.html')),

)
