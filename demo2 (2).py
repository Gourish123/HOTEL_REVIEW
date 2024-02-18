
import streamlit as st 
from textblob import TextBlob 
  
  
st.title("Sentiment Analysis for Hotel Review.") 
  
message = st.text_area("Please Enter your text") 
  
if st.button("Analyze the Sentiment"): 
  blob = TextBlob(message) 
  result = blob.sentiment 
  polarity = result.polarity 
  subjectivity = result.subjectivity 
  if polarity < 0: 
    st.warning("The entered text has negative sentiments associated with it:slightly_frowning_face:"+str(polarity)) 
    
  if polarity >= 0: 
    st.success("The entered text has positive sentiments associated with it:slightly_smiling_face:"+str(polarity)) 
    
  st.success(result)