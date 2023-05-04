# Import Library
import streamlit as st
from PyPDF2 import PdfFileReader #library pdf
import os

st.subheader("Halaman Upload")
st.write(
            """
            Silahkan Upload Dokumen
            """
        )

# Method atau fungsi save file
def save_upload(uploadedfile):
    with open(os.path.join("Documents/DataPdf",uploadedfile.name), "wb") as f:
        f.write(uploadedfile.getbuffer())
        return st.success("File berhasil disave: {} in Documents".format(uploadedfile.name))


doc_file = st.file_uploader("Upload Document", type=["pdf"])
if st.button("Proses"):
    if doc_file.type == "application/pdf":
             # Save File
             save_upload(doc_file)

             # Download File
             st.download_button(label='Download File',
                               data=doc_file,
                               file_name='My Documents.pdf',
                               mime='application/pdf')