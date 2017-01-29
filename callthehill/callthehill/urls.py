from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^issues/', include("issues.urls")),
    url(r'^legislation/', include("legislation.urls")),
    url(r'^activist/', include("activist.urls")),
    url(r'^phonebank/', include("phonebank.urls")),
    url(r'^feed/', include("feed.urls")),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
