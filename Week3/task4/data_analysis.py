import pandas as pd
import os
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine_uri = f"mysql+pymysql://{os.getenv('mysqluser')}:{os.getenv('mysqlpass')}@{os.getenv('mysqlhost')}/northwind"
    con = create_engine(engine_uri)
    order_table_query = "SELECT * FROM orders"
    details_query = "SELECT * FROM orderdetails"
    country_query = "SELECT DISTINCT ShipCountry FROM orders"
    customers_query = "SELECT * FROM customers"
    suppliers_query = "SELECT * FROM suppliers"
    customers_table = pd.read_sql(customers_query,con)
    suppliers_table = pd.read_sql(suppliers_query,con)
    order_table = pd.read_sql(order_table_query,con)
    details_table = pd.read_sql(details_query,con)
    countries = pd.read_sql(country_query,con)
    country_sales = []
    sales_pr_country = {}
    suppliers_pr_country = {}
    customer_pr_country = {}
    for country in countries["ShipCountry"]:
        sales_pr_country[country[:2]] = 0
        customer_pr_country[country[:2]]= len(customers_table[customers_table["Country"] == country])
        suppliers_pr_country[country[:2]] = len(suppliers_table[suppliers_table["Country"]==country])
        country_table = order_table[order_table["ShipCountry"] == country]
        for order_id in country_table["OrderID"]:
            sales_pr_country[country[:2]] = sales_pr_country[country[:2]] + details_table[details_table["OrderID"] == order_id]["Quantity"].iloc[0]
    plt.figure()
    plt.title("Sales pr country")
    sales_pr_country = dict(sorted(sales_pr_country.items() , key= lambda x:x[1],reverse=True))
    customer_pr_country = dict(sorted(customer_pr_country.items() , key= lambda x:x[1],reverse=True))
    suppliers_pr_country = dict(sorted(suppliers_pr_country.items() , key= lambda x:x[1],reverse=True))
    plt.bar(sales_pr_country.keys(), sales_pr_country.values())
    plt.figure()
    plt.title("Customer pr country")
    plt.bar(customer_pr_country.keys(),customer_pr_country.values())
    plt.figure()
    plt.title("Suppliers pr country")
    plt.bar(suppliers_pr_country.keys(),suppliers_pr_country.values())
    plt.show()
    con.dispose()

