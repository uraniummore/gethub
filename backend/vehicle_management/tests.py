from django.test import TestCase


# python manage.py test [app_name]
class VehicleManagementTests(TestCase):
    def test_example(self) -> None:
        result = 2 + 2
        self.assertEqual(result, 4)
