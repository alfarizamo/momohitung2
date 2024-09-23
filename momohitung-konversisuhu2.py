import streamlit as st

x = st.number_input("Masukkan nilai suhu")

sx = st.selectbox("Satuan awal", ["Celsius (C)", "Fahrenheit (F)", "Kelvin (K)"])

sy = st.selectbox("Satuan tujuan", ["Celsius (C)", "Fahrenheit (F)", "Kelvin (K)"])

sx_symbol = sx.split(" ")[-1][1]
sy_symbol = sy.split(" ")[-1][1]

y = 0

if sx_symbol == 'C':
    if sy_symbol == 'C':
        y = x 
    elif sy_symbol == 'F':
        y = x * 9/5 + 32 
    elif sy_symbol == 'K':
        y = x + 273.15 
elif sx_symbol == 'F':
    if sy_symbol == 'C':
        y = (x - 32) * 5/9  
    elif sy_symbol == 'F':
        y = x  
    elif sy_symbol == 'K':
        y = (x - 32) * 5/9 + 273.15  
elif sx_symbol == 'K':
    if sy_symbol == 'C':
        y = x - 273.15  
    elif sy_symbol == 'F':
        y = (x - 273.15) * 9/5 + 32 
    elif sy_symbol == 'K':
        y = x  

st.write(f"{x} {sx_symbol} = {y:.2f} {sy_symbol}")
