
import streamlit as st
import cmath

st.set_page_config(page_title="Equazioni di 2° grado - 4^R", page_icon="🧮")
st.title("🧮 Risolutore di Equazioni di Secondo Grado")
st.markdown("### M.G. per i suoi amici della 4^R 💙")

a = st.number_input("Inserisci il coefficiente a", value=1.0)
b = st.number_input("Inserisci il coefficiente b", value=0.0)
c = st.number_input("Inserisci il coefficiente c", value=0.0)

if st.button("Risolvi"):
    if a == 0:
        st.error("Errore: a non può essere zero.")
    else:
        delta = b**2 - 4*a*c
        if delta == 0:
            x = -b / (2*a)
            st.success(f"Un'unica soluzione reale:

x = {x}")
        else:
            x1 = (-b + cmath.sqrt(delta)) / (2*a)
            x2 = (-b - cmath.sqrt(delta)) / (2*a)
            st.success(f"Le soluzioni sono:

x1 = {x1}
x2 = {x2}")
