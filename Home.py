import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/WhatsApp Image 2023-04-05 at 7.39.12 AM.png")

with col2:
    st.title("Priya Khandnor")
    content = """Hi, I am Priya Khandnor! I pursuing computer science degree
    in guru nanak dev engineering college, bidar.Recently i completed my 
    powerbi course and python program.
    """
    st.info(content)
content2 = """Below you can find some of the apps I have built in python.Feel 
        free to contact me!"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write("[Source Code](https://pythonhow.com)")
