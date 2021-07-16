import streamlit as st 
from PIL import Image
import pickle
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#import tensorflow as tf
#from keras.preprocessing import image
from werkzeug.utils import secure_filename
st.set_option('deprecation.showfileUploaderEncoding', False)
#from keras.models import load_model

html_temp = """
   <div class="" style="background-color:salmon;" >
   <div class="clearfix">           
   <div class="col-md-12">
   <center><p style="font-size:40px;color:white;margin-top:10px;">Dikshant Mali - PIET18CS049</p></center> 
   <center><p style="font-size:30px;color:white;margin-top:10px;">Digital Image Processing End-Term Examination</p></center> 
   </div>
   </div>
   </div>
   """
st.markdown(html_temp,unsafe_allow_html=True)
  
st.title("""
        Collor Palette
         """
         )


img1= st.file_uploader("Please upload image", type=("jpg", "png"))
img2= st.file_uploader("Please upload image", type=("jpg", "png"))

if img1 is None:
  st.text("Please upload an Image 1")
else:
  file_bytes = np.asarray(bytearray(img1.read()), dtype=np.uint8)
  image = cv2.imdecode(file_bytes, 1)
  st.image(img1,caption='Uploaded Image 1', use_column_width=True)

if img2 is None:
  st.text("Please upload an Image 2")
else:
  file_bytes = np.asarray(bytearray(img2.read()), dtype=np.uint8)
  image = cv2.imdecode(file_bytes, 1)
  st.image(img2,caption='Uploaded Image 2', use_column_width=True)

option = st.selectbox('Choose Appropriate option',('Logical XOR', 'Logical AND'))

st.write('You selected:', option)


import cv2
from  PIL import Image, ImageOps
def import_and_predict():
  if option == "Logical XOR":
     result = cv2.bitwise_xor(img2, img1)
  else:
     result = cv2.bitwise_and(img1,img2)
  file_bytes = np.asarray(bytearray(result.read()), dtype=np.uint8)
  image = cv2.imdecode(file_bytes, 1)
  st.image(result,caption='Result', use_column_width=True)  
  
  return 0
    
if st.button("Click To Perform Operation"):
  result=import_and_predict()
  
if st.button("About"):
  st.header("Dikshant Mali")
  st.subheader("Student, Department of Computer Engineering, PIET")
html_temp = """
   <div class="" style="background-color:white;" >
   <div class="clearfix">           
   <div class="col-md-12">
   <center><p style="font-size:20px;color:black;margin-top:10px;">Digital Image processing EndTerm Lab</p></center> 
   </div>
   </div>
   </div>
   """
st.markdown(html_temp,unsafe_allow_html=True)
