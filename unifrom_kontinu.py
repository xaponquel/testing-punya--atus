import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


st.title("Distribusi Unifrom Kontinu")
st.sidebar.title("Distribution Parameters")
st.set_option('deprecation.showPyplotGlobalUse', False)


a = st.sidebar.number_input("Lower Bound (a)", min_value=-10.0, max_value=10.0, value=0.0, step=0.1)
b = st.sidebar.number_input("Upper Bound (b)", min_value=-10.0, max_value=10.0, value=1.0, step=0.1)
size = st.sidebar.number_input("Sample Size", min_value=30, max_value=10000, value=1000, step=100)


samples = np.random.uniform(low=a, high=b, size=size)


st.subheader(f"Histogram Distribusi Unifrom Kontinu (a={a}, b={b}, Sample Size={size})")
fig, ax = plt.subplots()
ax.hist(samples, bins='auto', density=True)
ax.set_xlabel('Value')
ax.set_ylabel('Density')
st.pyplot(fig)


st.subheader("Descriptive Statistics")
statistics = st.columns(2)
statistics[0].markdown(f"**Mean:** {np.mean(samples):.3f}")
statistics[1].markdown(f"**Standard Deviation:** {np.std(samples):.3f}")
