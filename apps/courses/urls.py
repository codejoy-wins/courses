from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^courses/destroy/(?P<course_id>\d+)$', views.destroy),
    url(r'^courses/confirm/(?P<course_id>\d+)$', views.confirm),
    url(r'^add$', views.add),

    url(r'^', views.odell)
]
