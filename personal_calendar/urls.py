# -*- coding: utf-8 -*-
import datetime

from django.conf.urls import patterns, include, url
from django.views.generic.edit import CreateView

from views import (delete_participant, delete, Evenement_List, Evenement_Detail)
from models import Evenement
from personal_calendar.forms import EventForm


urlpatterns = patterns('',
    url(r'^create/$', CreateView.as_view(model=Evenement, form_class=EventForm), name='update_create'),
    url(r'^(\d+)/update/$', CreateView.as_view(model=Evenement, form_class=EventForm), name='update_create'),
    url(r'^lists/$', Evenement_List.as_view(paginate_by=10), name='liste'),
    url(r'^lists/(?P<field>[\w-]+)/(?P<pattern>[\w-]+)/$',
        Evenement_List.as_view(paginate_by=10), name='liste'),
    url(r'^(\d+)/delete/$', delete, name='delete'),
    url(r'^(\d+)/participant/(\d+)/delete/$', delete_participant,
        name='delete_participant'),
    url(r'^(?P<pk>\d+)/detail/$', Evenement_Detail.as_view(), name='details'),
    )
