from django.urls import path

from Unit_and_integration_testing.main.views import CreateProfileView, ProfileListView, ProfileDetailsView

urlpatterns = [
    path('create/', CreateProfileView.as_view(), name='create_profile'),
    path('profile/list/', ProfileListView.as_view(), name='list_profiles'),
    path('profile/details<int:pk>/', ProfileDetailsView.as_view(), name='profile_details')
]