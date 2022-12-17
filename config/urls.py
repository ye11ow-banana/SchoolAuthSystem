from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('workers/', include('workers.urls')),
    path('students/', include('students.urls'))
]
