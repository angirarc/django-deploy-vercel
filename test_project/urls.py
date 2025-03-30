
from django.contrib import admin
from django.urls import path, include

from accounts.views import home, signup_view, login_view, logout_view

urlpatterns = [
    path('', home, name='home'),
    path('api/', include('api.urls')),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('admin/', admin.site.urls),
]
