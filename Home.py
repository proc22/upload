import streamlit as st

st.set_page_config(
    page_title="Multipage App",
    page_icon="👋",
)

st.title("Home")
st.sidebar.success("Pilih halaman di atas.")

st.subheader("Hai, Sahabat Kelas Awan Pintar :wave:")
    
st.write(
        "Saya bersemangat untuk menggunakan Streamlit lebih efisien dan efektif dalam bisnis."
    )
st.write("[Website Kelas Awan Pintar](https://kelasawanpintar.netlify.app/)")

st.write("---")

st.header("Apa yang saya lakukan")
st.write("##")
st.write(
            """
            Di Channel YouTube Kelas Awan Pintar, kita akan membuat tutorial untuk orang-orang yang:
            - sedang mencari cara untuk belajar Python.
            - sedang mencari cara untuk belajar Streamlit.
            - ingin belajar Analisis Data & Ilmu Data untuk melakukan analisis.
            - ingin belajar Artificial Intelligence, Data Science, Machine Learning, Natural Language Processing.
            - ingin belajar dunia IT
            - Jika ingin terhubung di [Linkedin](https://www.linkedin.com/in/jumadi-01/)
            - Jika ingin gabung di group telegram [Kelas Awan Pintar](https://t.me/+CdyAL5WlRVNjOGM1)


            Jika Channel YouTube saya menarik bagi Anda, jangan lupa untuk berlangganan dan menyalakan notifikasi, agar Anda tidak ketinggalan konten apa pun.
            
            [Channel YouTube](https://www.youtube.com/channel/UC7rCdlKnMTt26Q3np3rW1Iw)
            """
        )
st.header("Playlist Fundamental Streamlit")
col1, col2, col3 = st.columns(3)

with col1:
        st.subheader("Introduction di Aplikasi Streamlit")
        st.video('https://www.youtube.com/watch?v=0PBpAEGuNHM&list=PLm94WimySTnr_AllzUeBTZR-fdvTsw99l')

with col2:
        st.subheader("Cara menampilkan teks")
        st.video('https://www.youtube.com/watch?v=tPA0x_wToXQ&list=PLm94WimySTnr_AllzUeBTZR-fdvTsw99l&index=2')

with col3:
        st.subheader("Cara Menampilkan Data")
        st.video('https://www.youtube.com/watch?v=dIx4ccvKduU&list=PLm94WimySTnr_AllzUeBTZR-fdvTsw99l&index=3')
    
st.write("---")