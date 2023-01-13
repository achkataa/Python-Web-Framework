from django.test import TestCase

from django.core.exceptions import ValidationError

from Unit_and_integration_testing.main.models import Profile


class ProfileTests(TestCase):
    VALID_PROFILE_DATA = {
        'first_name': 'Angel',
        'last_name': 'Madin',
        'age': 17,
    }
    def test_profile_create_first_name_contains_only_letters_expect_success(self):
        profile = Profile(
            first_name=self.VALID_PROFILE_DATA['first_name'],
            last_name=self.VALID_PROFILE_DATA['last_name'],
            age=17,
        )

        profile.save()


    def test_profile_create_first_name_contains_digit_expect_to_fail(self):
        first_name = 'Angel1'
        profile = Profile(
            first_name=first_name,
            last_name=self.VALID_PROFILE_DATA['last_name'],
            age=self.VALID_PROFILE_DATA['age'],
        )

        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)



    def test_profile_create_first_name_contains_dollar_sign_expect_to_fail(self):
        first_name = 'Angel$'
        profile = Profile(
            first_name=first_name,
            last_name=self.VALID_PROFILE_DATA['last_name'],
            age=self.VALID_PROFILE_DATA['age']
        )

        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)

    def test_profile_full_name_when_correct_expect_success(self):
        profile = Profile(
            first_name='Angel',
            last_name='Madin',
            age=17,
        )

        self.assertEqual('Angel Madin', profile.full_name)