from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
]

# ^ : 문자열이 시작할 때
# $ : 문자열이 끝날 때
# \d : 숫자
# () : 패턴의 부분을 저장할 때
# ^post/ : url이(오른쪽부터) post/로 시작한다.
# (\ㅇ+) : 숫자가 있는데 이 숫자로 조회하고 찾을 수 있다.
# / : / 뒤에 문자가 있다.
# $ : url마지막이 / 로 끝난다.
