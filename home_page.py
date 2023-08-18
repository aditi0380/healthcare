import streamlit as st
import pandas

import streamlit as st

tab1, tab2 = st.tabs(["Logo", "Menu"])

with tab1:
   st.header("Logo")
   #st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
   st.header("Menu")
   #st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
   option = st.selectbox(
        'How would you like to be contacted?',
        ('GenData', 'MedicationAdherence', 'Nps','Obesity','PriorAuthFinal','ProdIsolation','Pto','V3'))
   st.write('You selected:', option)
   
# with tab3:
#    st.header("An owl")
#    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
