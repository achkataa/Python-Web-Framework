from django.contrib.auth import get_user_model

UserModel = get_user_model()
UserModel.objects.create_user(
    username='Angel',
    password='1234'
)
