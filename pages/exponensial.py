import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


st.title("Exponential Distribution")
st.sidebar.title("Distribution Parameters")
st.set_option('deprecation.showPyplotGlobalUse', False)


lam = st.sidebar.number_input("Lambda (Rate)", min_value=0.1, max_value=10.0, value=1.0, step=0.1)
size = st.sidebar.number_input("Sample Size", min_value=1, max_value=10000, value=1000, step=1)


samples = np.random.exponential(scale=1/lam, size=size)


st.subheader(f"Histogram of Exponential Distribution (Lambda={lam}, Sample Size={size})")
fig, ax = plt.subplots()
ax.hist(samples, bins='auto', density=True)
ax.set_xlabel('Value')
ax.set_ylabel('Density')
st.pyplot(fig)


st.subheader("Descriptive Statistics")
statistics = st.columns(2)
statistics[0].markdown(f"**Mean:** {np.mean(samples):.3f}")
statistics[1].markdown(f"**Standard Deviation:** {np.std(samples):.3f}")
