from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^$',views.index,name='index'),
  url(r'^add$',views.add,name='add'),
  url(r'^edit',views.edit,name='edit'),
  url(r'^group_add',views.group_add,name='group_add'),
  url(r'^saver',views.saver,name='saver'),
  url(r'^delete',views.delete,name='delete'),
]