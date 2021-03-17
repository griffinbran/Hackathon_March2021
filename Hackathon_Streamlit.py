import pickle
import streamlit as st
import numpy as np
import pandas as pd
import bz2
import _pickle as cPickle
#https://docs.streamlit.io/en/stable/api.html#display-data

st.set_page_config(
    page_icon=':fuelpump:',
    initial_sidebar_state='auto'
)

st.title('RMDS Hackathon')

page = st.sidebar.selectbox(
    'Select-A-Page',
    ('Overview', 'Models', 'About The Team')
)

#function


    
if page == 'Overview':
    st.subheader('Overview')
    st.write('''

Display of models and visualizations related to RMDS / WorldData.ai Data Science competition.

''')
    st.subheader('Use the drop-down menu on the left to explore')

    st.image('./images/oilrig.jpg', caption='''Photo by <a href="https://unsplash.com/@clydeo?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Clyde Thomas</a> on <a href="/s/photos/petroleum?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  ''', use_column_width=True)

elif page =='Models':
    st.subheader('Models')
    st.write('''
Use the checkboxes to select which features to include, then click "Run" to visualize the model.

Try it out for yourself:
    ''')

    d = st.checkbox('News Sentiment - Direct')
    i = st.checkbox('News Sentiment - Indirect')
    a = st.checkbox('Apple Mobility Data')
    g = st.checkbox('Google Mobility Data')
    c = st.checkbox('Commodity Pricing')


    lookup = pd.read_pickle('./compressed/books_look_p3')

    with open('./compressed/books_rec_small.pkl', 'rb') as f:
        recommender = pickle.load(f)

    with open('./compressed/books_text_dict.pkl', 'rb') as f:
        text = pickle.load(f)

    query = st.text_input('Please enter a word or phrase to search: ', max_chars=50)

    wout = st.text_input('If you would like to exclude a term from your results, please enter it here: ', max_chars=50)

    searched, recommendation = make_recs_new(query, wout)

    if type(recommendation) == str:
        st.write(recommendation) #if result is a string, print it
    else:
        st.write(searched) #show searched term
        st.table(recommendation) #if result is a df, show it

    st.write('''
    *SPACE FOR DATA DICTIONARY (IN TABLE FORMAT)
    ''')

elif page == 'About The Team':

    st.subheader('About The Team')
    st.write('''
Former GA DSI classmates (add text here)
    ''')

    #st.table(pd.read_pickle('./compressed/sample_pivot.pkl'))

    st.write('''
Brandon - (profile, optional image)
    ''')

    #st.image('./images/sample_vectors.png', use_column_width=True)

    st.write('''
Will - (profile, optional image)   
    ''')

    #st.image('./images/sample_vectors.png', use_column_width=True)

    st.write('''
+ James/Nader/Cloudy/Cristina 
    ''')
