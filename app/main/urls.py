from django.conf.urls import url
import views
urlpatterns = [
    url(r'^$', views.home),
    url(r'^test/$', views.home)
]
