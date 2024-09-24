import pandas as pd
import requests
import streamlit as st
import urllib.request
import json

url = 'https://www.saferproducts.gov/RestWebServices/'
query = 'Recall?format=json&Injury=Appliances'
response = urllib.request.urlopen(url+query)
response_bytes = response.read()
data5_dic = json.loads(response_bytes) 
response.close()
df5 = pd.DataFrame.from_dict(data5_dic)
#df5.head()
temp = df5['Importers']
cleared123 = []
for i in range(len(temp)):
    if len(temp[i])>0:
        values = []
        for j in range(len(temp[i])):
            values.append(temp[i][j]['Name'] )
        cleaned123.append(values)
    else:
        cleaned123.append('')
#df5['importers'] = cleared123 
#df5['remedy'] = cleaned123
cleared12 = df5['Importers'].value_counts()
print(cleared12)
#print(cleaned2)
st.title("sample")
st.write(df5['Importers'].value_counts())
