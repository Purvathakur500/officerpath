import streamlit as st
import psycopg2


def get_connection():
    return psycopg2.connect(
        host=st.secrets["ep-dawn-haze-azpyerpb.c-3.ap-southeast-1.aws.neon.tech"],
        database=st.secrets["neondb"],
        user=st.secrets["neondb_owner"],
        password=st.secrets["npg_k0Koqaen8dyw"],
        port=st.secrets["5432"],
        sslmode="require"
    )