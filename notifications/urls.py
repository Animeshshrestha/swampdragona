from django.urls import path, include
from django.contrib import admin
from demo.views import Notifications, user_login, logout_view

admin.autodiscover()

# urlpatterns = patterns('',
#     url(r'^admin/', include(admin.site.urls)),
# )
urlpatterns = [
	path('login/',user_login, name='hi'),
	path('logout/',logout_view,name='logout'),
	path('', Notifications.as_view(), name='home'),
	path('admin/', admin.site.urls)
]