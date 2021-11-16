from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

class AdminSiteTests(TestCase):
    
    def setup(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create.superuser(
            email = 'admin@gmail.com',
            password = 'pass123*'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email = 'test@gmail.com',
            password = '*pass123*',
            name='Test user'
        )
    
    def test_users_listed(self):
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)