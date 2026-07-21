import streamlit as st
st.title("แอปพลิเคชั่นแปลงปี พ.ศ. เป็น ค.ศ.")

bh_Year=st.number_imput("กรอกปี พ.ศ. ที่ต้องการแปลง"),value=2569
ce_Year=bh_year-543
st.header(f"ปี ค.ศ คือ : {ce_Year}")
