import streamlit as st
from st_files_connection import FilesConnection

# S3 Connection
conn = st.connection('s3', type=FilesConnection)
df = conn.read('mlops-bootcamp-datalake/final_online_retail.csv', input_format='csv', ttl=600)

def reset_session():
    st.session_state.client_type = None
    st.session_state.client_id = None

if 'client_type' not in st.session_state or 'client_id' not in st.session_state:
    reset_session()

if st.session_state.get("clear"):
    reset_session()
if st.session_state.get("cluster"):
    client_id = int(st.session_state.client_id)

    if client_id in df["customerid"].values:
        st.session_state.client_type = df[df["customerid"] == client_id]["labels"].values[0]
    else:
        st.session_state.client_type = "Client not found"


st.title("Online Retail Data 🛍️")
st.write("Input the client's ID to get the client type.")

st.text_input("Client ID", key="client_id")
st.write(f"Client Type: {st.session_state.client_type}")

st.button("Get Client Type", key="cluster")
st.button("Clear", key="clear")

