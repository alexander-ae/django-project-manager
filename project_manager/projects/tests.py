from django.contrib.auth.models import User
from django.test import Client
from django.core.urlresolvers import reverse
from .models import Project

from django.test.utils import override_settings
from django.test import TestCase


# @override_settings(DEBUG=True)
class ProjectTest(TestCase):
    @classmethod
    def setUpClass(self):
        self.client = Client
        self.demo_username = 'obi_wan_kenobi'
        self.demo_email = 'obi_wan@kenobi.com'
        self.demo_password = 'skywalker'

        self.project_name = 'Luke'

        super(ProjectTest, self).setUpClass()

    @classmethod
    def tearDownClass(self):
        # self.browser.quit()
        super(ProjectTest, self).tearDownClass()

    def test_new_project(self):
        """ Verificamos que al crear un proyecto, aparezca en el dashboard """

        self.u = User.objects.create(username=self.demo_username, email=self.demo_email, password='password')
        self.u.set_password(self.demo_password)
        self.u.save()

        self.client.login(username=self.demo_username, password=self.demo_password)

        project = Project.objects.create(name=self.project_name)

        response = self.client.get(reverse('dashboard:dashboard'))

        self.assertTrue(self.project_name in str(response.content))
