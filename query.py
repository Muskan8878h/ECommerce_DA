import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    username="root",
    password="root",
    database="ecommerce"
)

cur=db.cursor()

# 1. List all unique cities where customers are located.
query=""" select distinct customer_city from customers """
cur.execute(query)
data=cur.fetchall()
# print(data)


# 2. Count the number of orders placed in 2017.
query=""" select count(*) from orders where YEAR(order_purchase_timestamp)=2017 """
cur.execute(query)
data=cur.fetchall()
# print(data)


# 3. Find the total sales per category.
query=""" select products.product_category category, 
            round (sum(payments.payment_value),2) sales
            from products join order_items on
            products.product_id = order_items.product_id
            join payments on
            order_items.order_id = payments.order_id
            group by category
        """
cur.execute(query)
data=cur.fetchall() 
df=pd.DataFrame(data,columns=["Category","sales"])  #to frame the data
# print(df)


# 4. Calculate the percentage of orders that were paid in installments.
query=""" select 
            (sum(
                case when payment_installments >= 1 then 1 else 0 end
                ))/count(*)*100 from payments
        """
cur.execute(query)
data=cur.fetchall()
# print(data)


# 5. Count the number of customers from each state. 
query=""" select customer_state, count(customer_id) from customers
            group by customer_state
        """
cur.execute(query)
data=cur.fetchall()
df=pd.DataFrame(data,columns=["State","Number of Customers"])
print(df)
plt.bar(df["State"],df["Number of Customers"])
plt.xlabel("States")
plt.ylabel("Number of Customers")
plt.xticks(rotation=90)
plt.show()