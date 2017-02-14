from django.conf.urls import url
from django.contrib import admin

from final_project import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.introduce),
    url(r'^main/$', views.main),
    url(r'^about/$', views.about),
    url(r'^project/$', views.project),
    url(r'^contact/$', views.contact),
    url(r'^project1/$',views.project1),
url(r'^project2/$',views.project2),
url(r'^project3/$',views.project3),
url(r'^project4/$',views.project4),
url(r'^project5/$',views.project5),
url(r'^project6/$',views.project6),
url(r'^project7/$',views.project7),
url(r'^project8/$',views.project8),
url(r'^project9/$',views.project9),
url(r'^login$',views.login),
url(r'^login_check$',views.login_check),
]

