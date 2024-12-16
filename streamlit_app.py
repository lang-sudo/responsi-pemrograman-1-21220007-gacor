import streamlit as st

st.title("Hitung Keliling dan Luas")
st.write("Deskripsi")

panjang = st.number_input("Masukkan Panjang Persegi", value=0)
st.write("Panjang persegi: ", panjang)

lebar = st.number_input("Masukkan Lebar Persegi", value=0)
st.write("Lebar persegi: ", lebar)

if (lebar & panjang):
    st.subheader('keliling')
    st.write( 2 * ( panjang + lebar ) )

    st.subheader('Luas')
    st.write( panjang * lebar )
