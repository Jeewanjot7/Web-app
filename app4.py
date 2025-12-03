import streamlit as st
import pandas as pd
import numpy as np
 
st.title("Data Visualization Demo")
 
data = pd.DataFrame(np.random.randn(50, 2), columns=['A', 'B'])
#st.dataframe(data)
st.bar_chart(data)
st.line_chart(data)
st.area_chart(data)
 