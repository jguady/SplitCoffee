

from splitcoffee.model.MenuItem import MenuItem



def test_create_menu_item():
      menu_item_data = { "name": "Espresso", "price": 2.5 }
      menu_item = MenuItem(**menu_item_data)
      assert menu_item.name == menu_item_data["name"]
      assert menu_item.price == menu_item_data["price"]
