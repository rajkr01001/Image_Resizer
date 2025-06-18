import cv2
import streamlit as st 
import os
import numpy as np

st.title("Image Resizer App")
a=st.number_input("eneter your covert size")
ty=st.selectbox("enter your type",["KB","MB"])
img=st.file_uploader("Upload Image")
but=st.button("Convert")
if ty=="KB":
    b=1024
    z=1
    m=int(a)
elif ty=="MB":
    b=1024*1000
    print(b)
    m=1024*a
    print(a)
    z=500
if but:
    
    file_bytes = np.asarray(bytearray(img.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)

  
    i=1
    try:
        while i<b:
            resize=cv2.resize(img,(i,i))
            n=cv2.imwrite('test.jpg',resize)
            c=os.path.getsize('test.jpg')
            size=int(c/1024)
            print(size)
            i+=z
    
            if int(size) == int(m):
                with open('test.jpg', "rb") as f:
                    st.success(f"Click  download in {a}KB")
                    st.download_button("Download Image", f, file_name="resized.jpg")   
                  
                break

            elif int(size)>int(m):
                st.write(f"{a} {ty} not available please choise nearest size {a-2}{ty}to {a+2}{ty} and try again")
                with open('test.jpg', "rb") as f:
                    st.success("Click  download Nearest Size in MB")  
                    st.download_button("Download Image", f, file_name="resized.jpg")
                break 
    except Exception as e:
        st.write("SOMETHING ERROR PLEASE REFRESH TO TRY AGAIN")
        
hide_menu = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)
