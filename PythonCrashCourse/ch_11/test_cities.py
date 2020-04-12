import unittest
from city_functions import city_country

class CityNameTestCase(unittest.TestCase):
    def test_city_name(self):
        formatted_city_name = city_country('Medellin', 'Colombia')
        self.assertEqual(formatted_city_name, 'Medellin, Colombia - population ')
        
    def test_city_country_pop(self):
        formatted_city_info = city_country('Medellin', 'Colombia', '500000')
        self.assertEqual(formatted_city_info, 'Medellin, Colombia - population 500000')
        
unittest.main()