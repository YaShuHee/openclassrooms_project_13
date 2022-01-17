from django.urls import reverse
from django.test import TestCase


class OcLettingsSiteTest(TestCase):
    def test_oc_lettings_site_index_view(self):

        response = self.client.get(reverse("index"))
        assert response.status_code == 200

        assert b"<title>Holiday Homes</title>" in response.content

        assert b"<h1>Welcome to Holiday Homes</h1>" in response.content

        profile_a_tag = f"<a href=\"{reverse('profiles:index')}\">Profiles</a>"
        assert profile_a_tag.encode("UTF-8") in response.content

        letting_a_tag = f"<a href=\"{reverse('lettings:index')}\">Lettings</a>"
        assert letting_a_tag.encode("UTF-8") in response.content
