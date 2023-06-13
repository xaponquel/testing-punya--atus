import streamlit as st
from scipy import stats
import numpy as np


st.title('Z-Test')
st.write('Perform a Z-Test')


sample_mean = st.number_input('Sample Mean', step=0.01)
population_std = st.number_input('Population Standard Deviation', step=0.01)
sample_size = st.number_input('Sample Size', step=1)
significance_level = st.number_input('Significance Level', min_value=0.01, max_value=0.10, step=0.01)


z_score = (sample_mean - 0) / (population_std / np.sqrt(sample_size))
p_value = 2 * (1 - stats.norm.cdf(abs(z_score)))


if p_value < significance_level:
    st.write('Reject the null hypothesis')
else:
    st.write('Fail to reject the null hypothesis')


st.write('Z-Score:', z_score)
st.write('P-Value:', p_value)
