from django.test import TestCase
from django.urls import reverse
from .models import Articolo, Giornalista


class NewsViewsTests(TestCase):
	def setUp(self):
		self.giornalista = Giornalista.objects.create(
			nome="Ada",
			cognome="Rossi",
		)
		self.articolo = Articolo.objects.create(
			titolo="Notizia di prova",
			contenuto="Contenuto di prova",
			giornalista=self.giornalista,
		)

	def test_homepage_lists_articles_and_journalists(self):
		response = self.client.get(reverse("news:homeview"))

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, self.articolo.titolo)
		self.assertContains(response, str(self.giornalista))

	def test_article_detail_displays_article(self):
		response = self.client.get(
			reverse("news:articolo_detail", args=[self.articolo.pk])
		)

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, self.articolo.titolo)
		self.assertContains(response, self.articolo.contenuto)
