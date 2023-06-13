import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def main():
    st.title("Analisis Regresi Linier Sederhana dengan Visualisasi Model")

    st.subheader("Input Data:")
    x = st.text_input("Masukkan variabel x (pisahkan dengan koma)")
    y = st.text_input("Masukkan variabel y (pisahkan dengan koma)")

    
    x_values = [float(val.strip()) for val in x.split(',') if val.strip()]
    y_values = [float(val.strip()) for val in y.split(',') if val.strip()]

    
    if len(x_values) == 0 or len(y_values) == 0:
        st.error("Input data tidak valid!")
        return
    if len(x_values) != len(y_values):
        st.error("Jumlah data x dan y harus sama!")
        return

    
    df = pd.DataFrame({'x': x_values, 'y': y_values})

    st.subheader("Data:")
    st.write(df)

    
    feature_col = 'x'
    target_col = 'y'

   
    X = df[[feature_col]]
    y = df[target_col]

    
    if len(X) > 1:
    
        model = LinearRegression()
        model.fit(X, y)

        
        st.subheader("Koefisien dan Intersep:")
        st.write("Koefisien (slope):", model.coef_[0])
        st.write("Intersep (intercept):", model.intercept_)

       
        plt.figure(figsize=(8, 6))
        plt.scatter(X, y, color='b', label='Data')
        plt.plot(X, model.predict(X), color='r', label='Regresi Linier')
        plt.xlabel(feature_col)
        plt.ylabel(target_col)
        plt.title("Regresi Linier")
        plt.legend()
        st.subheader("Visualisasi Model:")
        st.pyplot(plt)
    else:
        st.warning("Data yang cukup tidak tersedia untuk membangun model.")

if __name__ == '__main__':
    main()
