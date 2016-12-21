from django.core.urlresolvers import resolve
from django.test import TestCase
from lists.views import HomePageView
from django.http.request import HttpRequest


# class SmokeTest(TestCase):  
#     def test_bad_maths(self): self.assertEqual(1 + 1, 3)
    

class HomePageTest(TestCase):
    
#     def test_url_resolve(self):
#         found = resolve('/')
#         self.assertEqual(found.func, HomePageView.as_view())
  
#     def test_url_resolve(self):
#          found = resolve('/')
#          self.assertEqual(found.func, HomePageView.home_page)
  
    
    def test_home_page_returns_correct_html(self):
        request = HttpRequest() #1
        response = HomePageView.home_page(request) #2
        self.assertTrue(response.content.startswith(b'<html>')) #3
        self.assertIn(b'<title>To-Do lists</title>', response.content)#4
        self.assertTrue(response.content.assertEndsWith(b'</html>'))#5