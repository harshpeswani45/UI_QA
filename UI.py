import streamlit as st
#import model here or use pickel or joblib to dump the model

st.set_option('deprecation.showfileUploaderEncoding',False)

html='''
<div style="background-color:SlateBlue;padding:10px">
<h2 style="color:white;text-align:center;"> Question Answering Testing App </h2>
</div>
<br>
<br> 
'''

st.markdown(html,unsafe_allow_html=True)

@st.cache(allow_output_mutation=True)
def load_model():
    #model=(load your model here)
    #return model
    return 0
with st.spinner('Loading Model Please Wait.....'):
    model=load_model()

question=st.text_input('Please enter your question here')
if question:
    st.write("Response:")
    with st.spinner("Fetching Responce....."):
        #prediction=model.predict() (fetch the answer (The question is in the question variable))
        st.success('Section Info = {}'.format('(Output :- Section Info )'))
        st.success('Answer = {}'.format('(Output:-Answer)'))
    st.write("")