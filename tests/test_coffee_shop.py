import pytest

from splitcoffee.CoffeeShop import CoffeeShop


def test_coffee_shop():
    coffee_shop = CoffeeShop()

def test_coffee_shop_menu_file_not_found():
    with pytest.raises(FileNotFoundError) as FNF:
        coffee_shop = CoffeeShop()
        coffee_shop.load_menu("gibberish")
    assert "No such file or directory" in str(FNF.value)

def test_coffee_shop_person_file_not_found():
    with pytest.raises(FileNotFoundError) as FNF:
        coffee_shop = CoffeeShop()
        coffee_shop.load_menu("teatime")
    assert "No such file or directory" in str(FNF.value)
