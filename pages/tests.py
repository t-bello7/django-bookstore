from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView

# Create your tests here.


class HomePageTests(SimpleTestCase):
    def setUp(self):
        url = reverse('home')
        self.view = resolve('/')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        # testing requests
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_url_name(self):
        # testing requests
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        # testing templates
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_contains_correct_html(self):

        # reads the elements of the pages
        self.assertContains(self.response, 'HomePage')

    def test_homepage_does_not_contain_incorrect_html(self):
        # reads the element not contained on the page
        self.assertNotContains(
            self.response, 'Hi there! I should not be on the page'
        )

    def test_homepage_url_resolves_homepageview(self):
        self.assertEqual(
            self.view.func.__name__,
            HomePageView.as_view().__name__
        )
