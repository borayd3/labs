import pandas as pd
import requests
import streamlit as st
import urllib.request
import json

url = 'https://www.saferproducts.gov/RestWebServices/'
query = 'Recall?format=json&RecallTitle=Gas'
response = urllib.request.urlopen(url+query)
response_bytes = response.read()
data2_dic = json.loads(response_bytes) 
response.close()
df4 = pd.DataFrame.from_dict(data2_dic)
temp = df4['RemedyOptions']
cleaned1 = []
for i in range(len(temp)):
    if len(temp[i])>0:
        values = []
        for j in range(len(temp[i])):
            values.append(temp[i][j]['Option'] )
        cleaned1.append(values[0])
    else:
        cleaned1.append('')
df4['remedy'] = cleaned1
cleaned2 = df4['remedy'].value_counts()
print(cleaned2)
st.title("sample")
st.write(cleaned2)
