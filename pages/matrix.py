import streamlit as st
import numpy as np

def matrix_addition(a, b):
    return np.add(a, b)

def matrix_subtraction(a, b):
    return np.subtract(a, b)

def matrix_multiplication(a, b):
    return np.dot(a, b)

def matrix_inverse(a):
    return np.linalg.inv(a)

st.title("Operasi Matriks")


st.header("Matriks A")
rows_a = st.number_input("Masukkan jumlah baris A", min_value=1, value=2, step=1)
cols_a = st.number_input("Masukkan jumlah kolom A", min_value=1, value=2, step=1)
matrix_a = np.zeros((rows_a, cols_a))

for i in range(rows_a):
    for j in range(cols_a):
        matrix_a[i][j] = st.number_input(f"Masukkan elemen A[{i+1}][{j+1}]")


st.header("Matriks B")
rows_b = st.number_input("Masukkan jumlah baris B", min_value=1, value=2, step=1)
cols_b = st.number_input("Masukkan jumlah kolom B", min_value=1, value=2, step=1)
matrix_b = np.zeros((rows_b, cols_b))

for i in range(rows_b):
    for j in range(cols_b):
        matrix_b[i][j] = st.number_input(f"Masukkan elemen B[{i+1}][{j+1}]")


st.header("Operasi")

operation = st.selectbox("Pilih operasi", ("Penjumlahan", "Pengurangan", "Perkalian", "Inversi"))

if operation == "Penjumlahan":
    if rows_a == rows_b and cols_a == cols_b:
        result = matrix_addition(matrix_a, matrix_b)
        st.header("Hasil Penjumlahan")
        st.write(result)
    else:
        st.warning("Ukuran matriks A dan B harus sama untuk penjumlahan.")

elif operation == "Pengurangan":
    if rows_a == rows_b and cols_a == cols_b:
        result = matrix_subtraction(matrix_a, matrix_b)
        st.header("Hasil Pengurangan")
        st.write(result)
    else:
        st.warning("Ukuran matriks A dan B harus sama untuk pengurangan.")

elif operation == "Perkalian":
    if cols_a == rows_b:
        result = matrix_multiplication(matrix_a, matrix_b)
        st.header("Hasil Perkalian")
        st.write(result)
    else:
        st.warning("Jumlah kolom matriks A harus sama dengan jumlah baris matriks B untuk perkalian.")

elif operation == "Inversi":
    if rows_a == cols_a:
        result = matrix_inverse(matrix_a)
        st.header("Hasil Inversi")
        st.write(result)
    else:
        st.warning("Matriks A harus persegi untuk inversi.")
