# pip install matplotlib
# pip install seaborn

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


myData = np.random.randn(30, 3)
df = pd.DataFrame(data = myData, columns=['x', 'y', 'z'])

'위에서 5개 데이터 :', df.head()

st.line_chart(df)

st.area_chart(df)

st.bar_chart(df)

''
'---'
''

df = pd.read_csv('data_iris.csv')
'붓꽃데이터', df.head()

cnts = df['Species'].value_counts()

fig = plt.figure(figsize=(7,5))
plt.bar(x=cnts.index, height=cnts.values, color='blue')
plt.ylable('Counts')
plt.title('Iris Flower Species Counts')
st.pyplot(fig)

fig2 = plt.figure(figsize=(7,5))
# legend = auto/brief/full
sns.countplot(x='Species', hue='Species', data=df, legend='brief')
plt.legend(loc='lower right')
st.pyplot(fig2)

