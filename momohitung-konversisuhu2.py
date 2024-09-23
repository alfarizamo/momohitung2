import streamlit as st

x = st.number_input("Masukkan nilai suhu")
sx = st.selectbox("Satuan awal", ["Celsius (C)", "Fahrenheit (F)", "Kelvin (K)", "Reamur (R)"])
sy = st.selectbox("Satuan tujuan", ["Celsius (C)", "Fahrenheit (F)", "Kelvin (K)", "Reamur (R)"])

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
    elif sy_symbol == 'R':
        y = x * 4/5 
        
elif sx_symbol == 'F':  
    if sy_symbol == 'C':
        y = (x - 32) * 5/9 
    elif sy_symbol == 'F':
        y = x  
    elif sy_symbol == 'K':
        y = (x - 32) * 5/9 + 273.15  
    elif sy_symbol == 'R':
        y = (x - 32) * 4/9  

elif sx_symbol == 'K': 
    if sy_symbol == 'C':
        y = x - 273.15 
    elif sy_symbol == 'F':
        y = (x - 273.15) * 9/5 + 32  
    elif sy_symbol == 'K':
        y = x  
    elif sy_symbol == 'R':
        y = (x - 273.15) * 4/5 

elif sx_symbol == 'R':  
    if sy_symbol == 'C':
        y = x * 5/4  
    elif sy_symbol == 'F':
        y = x * 9/4 + 32  
    elif sy_symbol == 'K':
        y = x * 5/4 + 273.15 
    elif sy_symbol == 'R':
        y = x  

else:
    st.write("Satuan yang dimasukkan tidak valid. Gunakan 'C', 'F', 'K', atau 'R'.")


st.write(f"{x} {sx_symbol} setara dengan:")
st.write(f"- {celsius:.2f} °C")
st.write(f"- {fahrenheit:.2f} °F")
st.write(f"- {kelvin:.2f} K")
st.write(f"- {reamur:.2f} °R")
