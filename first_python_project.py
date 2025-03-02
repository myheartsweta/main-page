import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mysql.connector

db=mysql.connector.connect(host="localhost",
                           username="root",
                           password="123456",
                           database="Ecommerce")
cur=db.cursor()



query="""select distinct customer_city from customers"""
cur.execute(query)
data=cur.fetchall()
print(data)

query="""select count(order_id)from orders where year(order_purchase_timestamp)=2017"""
cur.execute(query)
data=cur.fetchall()
print("total data placed in 2017",data)

query="""select products.product_category as category,
round(sum(payments.payment_value),2) as sales
from products join order_items
on products.product_id=order_items.product_id
join payments
on payments.order_id=order_items.order_id
group by category
"""

cur.execute(query)
data=cur.fetchall()

df=pd.DataFrame(data,columns=["category","sales"])
print(df)



query="""select sum(case when payment_installments >= 1 then 1 else 0 end)from payments"""
cur.execute(query)
data=cur.fetchall()
print(data)



query="""select customer_state,count(customer_id)
from customers group by customer_state"""
cur.execute(query)
data=cur.fetchall()
df=pd.DataFrame(data)
print(df)



query="""select customer_state,count(customer_id)
from customers group by customer_state"""
cur.execute(query)
data=cur.fetchall()
df=pd.DataFrame(data,columns=["state","customer_count"])
plt.bar(df["state"],df["customer_count"])
plt.show()


query="""select distinct customer_city from customers"""
cur.execute(query)
data=cur.fetchall()
df=pd.DataFrame(data)
df.head()



query="""select month(order_purchase_timestamp)months,count(order_id)order_count
from orders where year(order_purchase_timestamp)=2018
group by months"""
cur.execute(query)
data=cur.fetchall()
print(data)

query="""select month(order_purchase_timestamp)months,count(order_id)order_count
from orders where year(order_purchase_timestamp)=2018
group by months"""
cur.execute(query)
data=cur.fetchall()
df=pd.DataFrame(data,columns=["months","order_count"])
o=["january", "feb", "mar", "apr", "may", "june", "july", "aug", "sep", "oct", "nov", "dec"]
sns.barplot(x=df["months"],y=df["order_count"],data=df,order=o)
plt.show()










