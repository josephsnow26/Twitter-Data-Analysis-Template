import mysql.connector
import pandas as pd
import streamlit as st
import pandas as pd
import plotly.express as px

# # Connect to server
# conn = mysql.connector.connect(
#     host="localhost",
#     port=3306,
#     user="root",
#     password="160808037A",
#     database="monkey")

# # Get a cursor

# # Execute a query
st.set_page_config(page_title = 'Dashboard of employees and clients',
# page_icon = ':bar_chart:',
# layout = 'wide')
st.title('Dashboard of employees and clients')
# st.subheader('using python.')


# query1 = pd.read_sql('SELECT * FROM Employee;' , conn)
# st.header('Employees table')
# st.header('Distribution of the employees salary')

# sex = st.sidebar.multiselect('select the gender',
#                                 options = query1.Sex.unique(),
#                                 default = query1.Sex.unique()  )
# Sex_selection = query1.query(
#     'Sex == @sex'  
# )

# df1 = st.dataframe(Sex_selection)

# query10 = pd.read_sql('SELECT First_Name , Salary FROM Employee;' , conn)
# pp = px.bar(query10,
# y = query10.Salary,
# x = query10.First_Name,
# title = '<b>salary plot</b>')
# st.plotly_chart(pp)










# query5 = pd.read_sql('SELECT COUNT(Sex) AS TOTAL,Sex FROM Employee GROUP BY Sex;' , conn)
# st.header('Distribution of the employees genders')
# YY = px.bar(query5,
# y = query5.TOTAL,
# x = query5.Sex,
# title = '<b>Sex</b>')
# st.plotly_chart(YY)







# query0 = pd.read_sql('SELECT Employee.First_Name, SUM(Total_Sales) AS TOTAL FROM Works_With JOIN Employee ON Works_With.Emp_Id = Employee.Emp_Id GROUP BY Employee.First_Name;' , conn)

# st.header('Employees with the most sales to clients')
# pOp = px.bar(query0,
# y = query0.TOTAL,
# x = query0.First_Name,
# title = '<b>TOTAL SALES</b>')
# st.plotly_chart(pOp)


# query01 = pd.read_sql('SELECT SUM(Total_Sales) AS TOTAL,  Client.Client_Name FROM Works_with JOIN Client ON Works_with.Client_Id = Client.Client_Id GROUP BY Client.Client_Id;' , conn)

# query01

# st.header('Clients who spends the most with us')
# pOp = px.bar(query01,
# y = query01.TOTAL,
# x = query01.Client_Name,
# title = '<b>TOTAL SALES</b>')
# st.plotly_chart(pOp)






# # we close the cursor and conn both
# # mycursor.close()
# # conn.close()

