# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.test import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver

from .constants import LOGIN_URL, DASHBOARD_URL


class ProjectManagerAuthTests(LiveServerTestCase):
    # serialized_rollback = True

    @classmethod
    def setUpClass(self):
        self.browser = WebDriver()
        self.demo_username = 'obi_wan_kenobi'
        self.demo_email = 'obi_wan@kenobi.com'
        self.demo_password = 'skywalker'

        super(ProjectManagerAuthTests, self).setUpClass()

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        super(ProjectManagerAuthTests, self).tearDownClass()

    def test_login_username(self):
        """ Login por username """

        self.u = User.objects.create(username=self.demo_username, email=self.demo_email, password='passowrd')
        self.u.set_password(self.demo_password)
        self.u.save()

        self.browser.get('%s%s' % (self.live_server_url, LOGIN_URL))

        username_input = self.browser.find_element_by_name("username")
        username_input.send_keys(self.demo_username)

        password_input = self.browser.find_element_by_name("password")
        password_input.send_keys(self.demo_password)

        self.browser.find_element_by_xpath('//input[@type="submit"]').click()

        self.assertEqual(self.browser.current_url, '{}{}'.format(self.live_server_url, DASHBOARD_URL))

    def test_login_email(self):
        """ Login por email """

        self.u = User.objects.create(username=self.demo_username, email=self.demo_email, password='passowrd')
        self.u.set_password(self.demo_password)
        self.u.save()

        self.browser.get('%s%s' % (self.live_server_url, LOGIN_URL))

        username_input = self.browser.find_element_by_name("username")
        username_input.send_keys(self.demo_email)

        password_input = self.browser.find_element_by_name("password")
        password_input.send_keys(self.demo_password)

        self.browser.find_element_by_xpath('//input[@type="submit"]').click()
        self.assertEqual(self.browser.current_url, '{}{}'.format(self.live_server_url, DASHBOARD_URL))
