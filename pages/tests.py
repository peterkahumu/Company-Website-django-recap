from django.test import SimpleTestCase
from django.urls import reverse

class HomepageTests(SimpleTestCase):
    """Test cases for the Home page view."""
    def setUp(self):
        self.response_path = self.client.get('/')
        self.response_name = self.client.get(reverse('home'))

    def test_url_at_correct_location(self):
        """Homepage loads successfully at the root URL ('/')."""
        self.assertEqual(self.response_path.status_code, 200)
    
    def test_url_available_by_name(self):
        """Homepage loads successfully using its URL name 'home'."""
        self.assertEqual(self.response_name.status_code, 200)
    
    def test_correct_template_used(self):
        """Ensure that the home.html template is the one being used."""
        self.assertTemplateUsed(self.response_name, 'home.html')
    
    def test_template_content(self):
        """Ensure that the template contains a predefined message."""
        self.assertContains(self.response_name, "<h1>Company Website</h1>")


class AboutPageTests(SimpleTestCase):
    """Test cases for the About page view."""
    def setUp(self):
        self.response = self.client.get(reverse('about'))

    def test_url_at_correct_location(self):
        """About page loads successfully at '/about/'."""
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
    
    def test_url_available_by_name(self):
        """About page loads successfully using its URL name 'about'."""
        self.assertEqual(self.response.status_code, 200)
    
    def test_correct_template_used(self):
        """Ensure that the template used is 'about.html' """
        self.assertTemplateUsed(self.response, 'about.html')
    
    def test_template_content(self):
        """Ensure the template used has predefined input."""
        self.assertContains(self.response, '<h1>Company About Page </h1>')
