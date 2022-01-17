from django.urls import reverse
from django.test import TestCase

from .models import Address, Letting


class LettingsTest(TestCase):
    def setUp(self):
        self.address = Address.objects.create(
            number=1,
            street="Place de la Victoire",
            city="Bordeaux",
            state="France",
            zip_code="33000",
            country_iso_code="FR"
        )
        self.letting = Letting.objects.create(
            title="Not exactly holidays",
            address=self.address
        )

    def test_lettings_index_view(self):

        response = self.client.get(reverse("lettings:index"))

        assert response.status_code == 200
        assert b"<title>Lettings</title>" in response.content

        detail_a_tag = "<a href=\""
        f"{reverse('lettings:letting', kwargs={'letting_id': self.letting.id})}"
        f"\">{self.letting.title}</a>"
        assert detail_a_tag.encode("UTF-8") in response.content

    def test_lettings_detail_view(self):

        response = self.client.get(reverse("lettings:letting", kwargs={"letting_id": 1}))

        assert response.status_code == 200
        assert f"<title>{self.letting.title}</title>".encode("UTF-8") in response.content

        assert f"<h1>{self.letting.title}</h1>".encode("UTF-8") in response.content
        assert f"<p>{self.address.number} {self.address.street}</p>".encode("UTF-8")\
               in response.content
        region_p_tag = f"<p>{self.address.city}, {self.address.state} {self.address.zip_code}</p>"
        assert region_p_tag.encode("UTF-8") in response.content
        assert f"<p>{self.address.country_iso_code}</p>".encode("UTF-8") in response.content
