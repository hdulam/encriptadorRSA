import streamlit as st
from rsa import encriptar, desencriptar

st.title("Parcial 3 Matematica Discreta")

tab1, tab2 = st.tabs(["Encriptar", "Desencriptar"])

with tab1:
    msg = st.text_input("Mensaje M")
    p = st.text_input("p", key="p1")
    q = st.text_input("q", key="q1")
    e = st.text_input("e", key="e1")
    if st.button("Encriptar"):
        try:
            C, L, txt = encriptar(msg, p, q, e)
            st.write("Cifrado C:")
            st.code(C)
            st.write("Longitud L:")
            st.code(L)
            st.write("Detalle:")
            st.code(txt)
        except ValueError as err:
            st.error(err)

with tab2:
    C = st.text_input("Cifrado C")
    L = st.text_input("Longitud L")
    p = st.text_input("p", key="p2")
    q = st.text_input("q", key="q2")
    e = st.text_input("e", key="e2")
    if st.button("Desencriptar"):
        try:
            msg, txt = desencriptar(C, L, p, q, e)
            st.write("Mensaje M:")
            st.code(msg)
            st.write("Detalle:")
            st.code(txt)
        except ValueError as err:
            st.error(err)
