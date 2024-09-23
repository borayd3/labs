import pandas as pd
import requests
import streamlit as st
    # Conduct analysis:
url = 'https://www.saferproducts.gov/RestWebServices/Recall'
query = '?format=json&RecallTitle=Gas'
header = {'User-Agent':
          'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0'}
raw = requests.get(url+query,headers=header)
data = raw.json()
df = pd.DataFrame.from_dict(data)
temp = df['RemedyOptions']
clean_values = []
for i in range(len(temp)):
    if len(temp[i])>0:
        values = []
        for j in range(len(temp[i])):
            values.append(temp[i][j]['Option'] )
        clean_values.append(values)
    else:
        clean_values.append('')
df['remedy'] = clean_values
remedy_counts = df['remedy'].value_counts()
    # Create streamlit output:
st.title('Remedy Statistics')
st.write(remedy_counts)