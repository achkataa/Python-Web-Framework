from django.test import TestCase
from django.urls import reverse

from Unit_and_integration_testing.main.models import Profile


class TestCreateProfile(TestCase):
    def test_create_profile_when_valid_expect_success(self):
        profile_data = {
            'first_name': 'Angel',
            'last_name': 'Madin',
            'age': 17,
        }

        response = self.client.post(reverse('create_profile'), data=profile_data)

        profile = Profile.objects.first()

        self.assertIsNotNone(profile)
        self.assertEqual(profile_data['first_name'], profile.first_name)
        self.assertEqual(profile_data['last_name'], profile.last_name)
        self.assertEqual(profile_data['age'], profile.age)



