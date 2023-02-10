from main import init
import pytest
import model
from main import show_clients
from main import show_orders
import main 


def test_checking_of_init_tables():
    assert init()=="Table has been created!"

def test_count_of_clients():
    main.fill()
    assert show_clients()>=10
    
def test_count_of_orders():
    main.fill()
    assert show_orders()>=10

def test_clients():
    assert model.CLIENTS.name == True
    assert model.CLIENTS.city == True
    assert model.CLIENTS.address == True

def test_orders(): 
    assert model.ORDERS.client == True
    assert model.ORDERS.amount == True
    assert model.ORDERS.date == True
    assert model.ORDERS.description == True
