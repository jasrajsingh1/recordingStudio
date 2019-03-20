from django.conf.urls import url
from django.contrib import admin

from dodra_rec_studio import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^admin/', admin.site.urls),
]