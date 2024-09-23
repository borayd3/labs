import pandas as pd
import requests
import streamlit as st
import urllib.request
import json

url = 'https://www.saferproducts.gov/RestWebServices/'
query = 'Recall?format=json&Manufacturer=Beds'
response = urllib.request.urlopen(url+query)
response_bytes = response.read()
data2 = json.loads(response_bytes) 
response.close()

df2 = pd.DataFrame.from_dict(data2)
df2.head()

temp1 = df2['RemedyOptions']
clean_values1 = []
for i in range(len(temp1)):
    if len(temp1[i])>0:
        values1 = []
        for j in range(len(temp1[i])):
            values1.append(temp1[i][j]['Option'] )
        clean_values1.append(values1)
    else:
        clean_values1.append('')
df2['remedy'] = clean_values1
remedy_counts = df2['remedy'].value_counts()
st.title('Remedy Statistics')
st.write(remedy_counts)