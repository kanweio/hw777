from django.contrib import admin
from django.urls import path, include
from . import swagger

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('movie_app.urls')),
    path('users/', include('users.urls'))
]

urlpatterns += swagger.urlpatterns