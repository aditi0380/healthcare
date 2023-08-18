import streamlit as st
import pandas


# tab1, tab2 = st.tabs(["Logo", "Menu"])

# with tab1:
#    st.header("Logo")
#    #st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

# with tab2:
#    #st.header("Menu")
#    #st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
#    option = st.selectbox(
#         'How would you like to be contacted?',
#         ('GenData', 'MedicationAdherence', 'Nps','Obesity','PriorAuthFinal','ProdIsolation','Pto','V3'))
#    st.write('You selected:', option)
   
# with tab3:
#    st.header("An owl")
#    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

# import streamlit.components.v1 as components
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">',unsafe_allow_html=True)

st.markdown("""
<nav class="navbar navbar-expand-lg navbar-light bg-light" style="background-color: #3498DB;>
  <div class="container-fluid">
    <a class="navbar-brand">Navbar</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Link</a>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Dropdown
          </a>
          <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
            <li><a class="dropdown-item" href="#">Action</a></li>
            <li><a class="dropdown-item" href="#">Another action</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="#">Something else here</a></li>
          </ul>
        </li>
      </ul>
    </div>
  </div>
</nav>
""", unsafe_allow_html=True)

# components.html(
#     """
#     <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
#     <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
#     <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
#     <ul class="nav nav-tabs">
#   <li class="nav-item">
#     <a class="nav-link active" aria-current="page" href="#">Active</a>
#   </li>
#   <li class="nav-item dropdown">
#     <a class="nav-link dropdown-toggle" data-bs-toggle="dropdown" role="button" aria-expanded="false">Dropdown</a>
#     <ul class="dropdown-menu">
#       <li><a class="dropdown-item" href="#">Action</a></li>
#       <li><a class="dropdown-item" href="#">Another action</a></li>
#       <li><a class="dropdown-item" href="#">Something else here</a></li>
#       <li><hr class="dropdown-divider"></li>
#       <li><a class="dropdown-item" href="#">Separated link</a></li>
#     </ul>
#   </li>
#   <li class="nav-item">
#     <a class="nav-link" href="#">Link</a>
#   </li>
#   <li class="nav-item">
#     <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Disabled</a>
#   </li>
# </ul>
#    """
# )

