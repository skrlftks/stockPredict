import streamlit as st
import pandas as pd

myFile = st.file_uploader("엑셀 파일을 선택하세요")
out = st.empty()

# openpyxl 설치
# pip install openpyxl
if myFile:
    out.write("xlxs 파일 한개를 업로드 햇습니다~")
    df = pd.read_excel(myFile, engine='openpyxl')
    st.write(df)


myFile2 = st.file_uploader("CSV 파일을 선택하세요")
out2 = st.empty()
if myFile:
    out.write("CSV 파일 한개를 업로드 햇습니다~")
    cdf = pd.read_csv(myFile2)
    st.write(cdf)