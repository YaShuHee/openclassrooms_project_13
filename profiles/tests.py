from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User

from .models import Profile


class ProfilesTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="Tim",
            password="test"
        )
        self.profile = Profile.objects.create(
            user=self.user,
            favorite_city="Bordeaux"
        )

    def test_profiles_index_view(self):

        response = self.client.get(reverse("profiles:index"))

        assert response.status_code == 200
        assert b"<title>Profiles</title>" in response.content

        detail_a_tag = f"<a href=\""
        f"{reverse('profiles:profile', kwargs={'username': self.profile.user.username})}"
        f"\">{self.profile.user.username}</a>"
        assert detail_a_tag.encode("UTF-8") in response.content

    def test_profiles_detail_view(self):

        response = self.client.get(reverse("profiles:profile", kwargs={"username": "Tim"}))

        assert response.status_code == 200
        assert f"<title>{self.profile.user.username}</title>".encode("UTF-8") in response.content

        assert f"<h1>{self.profile.user.username}</h1>".encode("UTF-8") in response.content
        assert f"<p>First name: {self.profile.user.first_name}</p>".encode("UTF-8")\
               in response.content
        assert f"<p>Last name: {self.profile.user.last_name}</p>".encode("UTF-8")\
               in response.content
        assert f"<p>Email: {self.profile.user.email}</p>".encode("UTF-8") in response.content
        assert f"<p>Favorite city: {self.profile.favorite_city}</p>".encode("UTF-8")\
               in response.content
