# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.test import Client

from .constants import LOGIN_URL, DASHBOARD_URL

from django.test.utils import override_settings
from django.test import TestCase


# @override_settings(DEBUG=True)
class ProjectManagerAuthTests(TestCase):
    @classmethod
    def setUpClass(self):
        self.client = Client
        self.demo_username = 'obi_wan_kenobi'
        self.demo_email = 'obi_wan@kenobi.com'
        self.demo_password = 'skywalker'

        super(ProjectManagerAuthTests, self).setUpClass()

    @classmethod
    def tearDownClass(self):
        # self.browser.quit()
        super(ProjectManagerAuthTests, self).tearDownClass()

    def test_login_username(self):
        """ Login por username """

        self.u = User.objects.create(username=self.demo_username, email=self.demo_email, password='password')
        self.u.set_password(self.demo_password)
        self.u.save()

        self.client.login(username=self.demo_username, password=self.demo_password)

        response = self.client.get(LOGIN_URL)

        self.assertRedirects(response, DASHBOARD_URL)

    def test_login_error(self):
        """ Login por email """

        self.u = User.objects.create(username=self.demo_username, email=self.demo_email, password='password')
        self.u.set_password(self.demo_password)
        self.u.save()

        login = self.client.login(username=self.demo_username, password='error')
        self.assertFalse(login)

        response = self.client.get(LOGIN_URL)
        self.assertEqual(response.status_code, 200)
