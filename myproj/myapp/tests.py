from django.test import TestCase
from myapp.models import Animal


class AnimalTestCase(TestCase):
  def setUp(self):
   Animal.objects.create(name="lion", voice="roar")
   Animal.objects.create(name="cat", voice="meow")
  def test_animals_can_speak(self):
     """Animals that can speak are correctly identified"""
     lion = Animal.objects.get(name="lion")
     cat = Animal.objects.get(name="cat")
     self.assertEqual(lion.speak(10), 200)
     self.assertEqual(cat.speak(10), 200)




