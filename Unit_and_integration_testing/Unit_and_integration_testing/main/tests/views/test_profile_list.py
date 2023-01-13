from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from Unit_and_integration_testing.main.models import Profile

Usermodel = get_user_model()

class TestListProfiles(TestCase):
    def test_get_expect_correct_template(self):
        response = self.client.get(reverse('list_profiles'))
        self.assertTemplateUsed(response, 'profile_list.html')

    def test_when_two_profiles_expect_two_profiles(self):
        profiles_to_create = (
            Profile(first_name='Angel', last_name='Madin', age=17),
            Profile(first_name='Gosho', last_name='Goshov', age=18),
        )

        Profile.objects.bulk_create(profiles_to_create)

        response = self.client.get(reverse('list_profiles'))

        profiles = response.context['object_list']

        self.assertEqual(len(profiles), 2)

    def test_get_when_not_logged_in_user_context_expected_to_be_No_user(self):
        response = self.client.get(reverse('list_profiles'))

        self.assertEqual('No user', response.context['user'])

    def test_get_when_user_logged_in_context_expected_to_be_the_username_of_the_user(self):
        user_data = {
            'username': 'Angel1',
            'password': '1234A1234m',
        }

        Usermodel.objects.create_user(**user_data)

        self.client.login(**user_data)

        response = self.client.get(reverse('list_profiles'))

        user = response.context['user']

        self.assertEqual(user_data['username'], user)







