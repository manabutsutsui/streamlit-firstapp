import streamlit as st
import numpy as np
import pandas as pd

st.title('Streamlit初心者')
st.subheader('ドキュメントをしっかり読むことを意識します。')

df = pd.DataFrame(
    np.random.randn(50, 2) / [50, 50] + [35.76, 139.76],
    columns=['lat', 'lon'])


if st.checkbox('マップを表示'):
    st.map(df)