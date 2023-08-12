from django.test import TestCase
from django.test import RequestFactory
from django.contrib.auth.models import AnonymousUser, User
from restaurant.models import Menu
from restaurant.views import MenuItemsView


class MenuViewTest(TestCase):
    def setUp(self):
        menu_list = []
        pizza = Menu.objects.create(title="Pizza", price=80, inventory=100)
        lasagna = Menu.objects.create(title="Lasagna", price=23, inventory=456)
        spaguetti = Menu.objects.create(title="Spaguetti", price=58, inventory=123)
        menu_list.append(pizza)
        menu_list.append(lasagna)
        menu_list.append(spaguetti)
        self.menu_list = menu_list
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username="jacob", email="jacob@…", password="top_secret"
        )
    
    def test_getall(self):
        request = self.factory.get("/api/menu")
        request.user = self.user
        response = MenuItemsView.as_view()(request)
        self.assertEqual(response.status_code, 200)
