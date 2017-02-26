""" project_manager URL Configuration """

from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'^auth/', include('project_manager_auth.urls', namespace='project_manager_auth')),
                  url(r'', include('dashboard.urls', namespace='dashboard')),
                  url(r'', include('projects.urls', namespace='projects')),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
