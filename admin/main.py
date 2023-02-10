import datetime
from model import *


def init():
    creation = "Empty space"
    with db:
        db.drop_tables([CLIENTS,ORDERS])
        db.create_tables([CLIENTS,ORDERS])
        print("Table has been created!")
        creation = "Table has been created!"
    return creation

def fill():
        with db:
            clients = [{'name':'Jerry','city': '*******', 'address':'*******'},
            {'name':'Altair','city': '*******', 'address':'*******'},
            {'name':'Sarah','city': '*******', 'address':'*******'},
            {'name':'Misha','city': '*******', 'address':'*******'},
            {'name':'Alexander','city': '*******', 'address':'*******'},
            {'name':'Crimson','city': '*******', 'address':'*******'},
            {'name':'Kenny','city': '*******', 'address':'*******'},
            {'name':'Sophia','city': '*******', 'address':'*******'},
            {'name':'Rick','city': '*******', 'address':'*******'},
            {'name':'Deen','city': '*******', 'address':'*******'},
            {'name':'Samuel','city': '*******', 'address':'*******'},
            {'name':'Romeo','city': '*******', 'address':'*******'},
            {'name':'Sanchez','city': '*******', 'address':'*******'}]
            CLIENTS.insert_many(clients).execute()
        with db:   
            clients = CLIENTS.select() 
            orders=[{'client': clients[0],'date':datetime.date(2023, 1, 5),'amount': 1,'description':'heavy'},
                    {'client': clients[1],'date':datetime.date(2023, 1, 14),'amount': 3,'description':'light'},
                    {'client': clients[2],'date':datetime.date(2023, 1, 14),'amount': 1,'description':'light'},
                    {'client': clients[3],'date':datetime.date(2023, 1, 15),'amount': 2,'description':'light'},
                    {'client': clients[4],'date':datetime.date(2023, 1, 18),'amount': 1,'description':'heavy'},
                    {'client': clients[5],'date':datetime.date(2023, 1, 19),'amount': 1,'description':'heavy'},
                    {'client': clients[6],'date':datetime.date(2023, 1, 22),'amount': 1,'description':'heavy'},
                    {'client': clients[7],'date':datetime.date(2023, 1, 23),'amount': 12,'description':'medium'},
                    {'client': clients[8],'date':datetime.date(2023, 1, 25),'amount': 30,'description':'light'},
                    {'client': clients[9],'date':datetime.date(2023, 1, 29),'amount': 5,'description':'light'},
                    {'client': clients[10],'date':datetime.date(2023, 1, 29),'amount': 5,'description':'light'},
                    {'client': clients[11],'date':datetime.date(2023, 3, 29),'amount': 5,'description':'light'},
                    {'client': clients[12],'date':datetime.date(2023, 1, 30),'amount': 5,'description':'medium'}]
            ORDERS.insert_many(orders).execute()
            print("Tables are filled!")




def show_clients():
    for client in CLIENTS.select():
        print(client.name,client.city,client.address)
    return CLIENTS.select().count()

    

def show_orders():
    for order in ORDERS.select():
        print(order.client,order.date,order.amount,order.description)
    return ORDERS.select().count()

def output():
    if check == "init":
        init()
    elif check == "show orders" or check == "Show Orders" or check == "Show orders" or check == "show Orders" or check == "SHOW ORDERS":
        show_orders()
    elif check == "show clients" or check == "Show Clients" or check == "Show clients" or check == "show Clients" or check == "SHOW CLIENTS":
        show_clients()
    elif check == "fill":
        fill()

if __name__ == "__main__":
    print("init - to create or recreate a table")
    print("fill - to fill a table")
    print("show * - to show created and filled stuff")
    print("* = 'clients' or 'orders'")
    print("Enter a command for your needs: ")
    check=input()
    output()

