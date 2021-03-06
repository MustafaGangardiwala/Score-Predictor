import streamlit as st
import pandas as pd 
import numpy as np
import pickle as pkl
import altair as alt

pickle_in = open('regressor.pickle', 'rb')
regressor = pkl.load(pickle_in)
pickle_in.close()



def main():

    st.set_page_config(page_title='Score Predictor',  layout = 'centered', initial_sidebar_state = 'auto')
    html_temp = """
    <div style="background-color:#f63366 ;padding:10px">
    <h2 style="color:white;text-align:center;">Score Predictor</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    st.text("This application predicts the score(1-100) of student based on number of hours they study")
    st.text("Using Streamlit")

    url = 'https://raw.githubusercontent.com/AdiPersonalWorks/Random/master/student_scores%20-%20student_scores.csv'
    df = pd.read_csv(url)

    if st.checkbox('Show Dataset'):
        st.header('Dataset')
        st.table(df)

    if st.checkbox('Show Scatter Plot'):
        st.header('Scatter Plot')
        st.altair_chart(alt.Chart(df).mark_circle(size=25).encode(x='Hours', y='Scores'))

    st.header('Add number of hours/day of studying')
    hours = st.slider("Enter Hours/Day",0.0,10.0,9.25,.25)

    st.success("PREDICTED SCORE OF THE STUDENT: {}".format(regressor.predict([[hours]])))

    st.info("""\
          
        By: [LinkedIn](https://www.linkedin.com/in/mustafa-gangardiwala/) |
         [Gmail](mailto:gangardiwalam.mg@gmail.com) |
         Source: [GitHub](https://github.com/MustafaGangardiwala/Score-Predictor)
        | Data Source: [GitHub](https://raw.githubusercontent.com/AdiPersonalWorks/Random/master/student_scores%20-%20student_scores.csv). 
    """)
   
if __name__ == "__main__":
    main()