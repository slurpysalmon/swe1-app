from django.test import TestCase

from django.urls import reverse


class PollsSmokeTests(TestCase):
    def test_index_page_status_code(self):
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)

    def test_detail_page_not_found_for_missing_question(self):
        response = self.client.get(reverse("polls:detail", args=(9999,)))
        self.assertEqual(response.status_code, 404)

    def test_dummy(self):
        self.assertTrue(False)
