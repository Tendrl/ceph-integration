from django.conf.urls import patterns, include, url
from rest_framework import routers
from ceph import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'user', views.UserViewSet)
router.register(r'cluster', views.ClusterViewSet, base_name='cluster')
router.register(r'pool', views.PoolViewSet, base_name='cluster/(?P<fsid>[a-zA-Z0-9-]+)/pool')


urlpatterns = patterns(
    '',
    url(r'^user/me', views.user_me),
    url(r'^', include(router.urls)),
    #url(r'^cluster$', views.ClusterViewSet.as_view({'get': 'list'})),
    #url(r'^cluster/(?P<fsid>[a-zA-Z0-9-]+)$', views.ClusterViewSet.as_view({'get': 'detail'})),
    url(r'^cluster/(?P<fsid>[a-zA-Z0-9-]+)/osd_map', views.OSDMap.as_view(), name='cluster-osd-map'),
    url(r'^cluster/(?P<fsid>[a-zA-Z0-9-]+)/health$', views.Health.as_view(), name='cluster-health'),
    url(r'^cluster/(?P<fsid>[a-zA-Z0-9-]+)/health_counters$', views.HealthCounters.as_view(),
        name='cluster-health-counters'),
    url(r'^cluster/(?P<fsid>[a-zA-Z0-9-]+)/space$', views.Space.as_view(), name='osd-space'),
    url(r'^cluster/(?P<fsid>[a-zA-Z0-9-]+)/osd$', views.OSDList.as_view(), name='cluster-osd-list'),
    url(r'^cluster/(?P<fsid>[a-zA-Z0-9-]+)/osd/(?P<osd_id>\d+)$', views.OSDDetail.as_view(),
        name='cluster-osd-detail'),

    url(r'^cluster/(?P<fsid>[a-zA-Z0-9-]+)/pool$', views.PoolViewSet.as_view({'get': 'list'}),
        name='cluster-pool-list'),
    url(r'^cluster/(?P<fsid>[a-zA-Z0-9-]+)/pool/(?P<pool_id>\d+)$', views.PoolViewSet.as_view({'get': 'retrieve'}),
        name='cluster-pool-detail'),
)