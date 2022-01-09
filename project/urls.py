from django.contrib import admin
from django.urls import path

from przyklad import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v.przyklad)
]
