import pandas as pd
import requests
import streamlit as st
import urllib.request
import json

url = 'https://www.saferproducts.gov/RestWebServices/'
query = 'Recall?format=json&Manufacturer=Beds'
response = urllib.request.urlopen(url+query)
response_bytes = response.read()
data22 = json.loads(response_bytes) 
response.close()

df = pd.DataFrame.from_dict(data2)
df.head()

temp1 = df['RemedyOptions']
clean_values1 = []
for i in range(len(temp1)):
    if len(temp1[i])>0:
        values1 = []
        for j in range(len(temp1[i])):
            values1.append(temp1[i][j]['Option'] )
        clean_values1.append(values1)
    else:
        clean_values1.append('')
df['remedy'] = clean_values1
remedy_counts = df['remedy'].value_counts()
st.title('Remedy Statistics')
st.write(remedy_counts)