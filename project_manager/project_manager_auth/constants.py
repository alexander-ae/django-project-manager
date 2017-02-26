# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse_lazy


DASHBOARD_URL = reverse_lazy('dashboard:dashboard')
LOGIN_URL = reverse_lazy('project_manager_auth:login')
LOGOUT_URL = reverse_lazy('project_manager_auth:logout')
