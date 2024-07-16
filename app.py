import streamlit as st
import pickle
import pandas as pd


teams = ['Sunrisers Hyderabad',
 'Mumbai Indians',
 'Royal Challengers Bangalore',
 'Kolkata Knight Riders',
 'Kings XI Punjab',
 'Chennai Super Kings',
 'Rajasthan Royals',
 'Delhi Capitals']

cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
       'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
       'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
       'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
       'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
       'Sharjah', 'Mohali', 'Bengaluru']

pipe = pickle.load(open('pipe.pkl','rb'))
st.title('IPL Win Predictor')

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select the batting team',sorted(teams))
with col2:
    bowling_team = st.selectbox('Select the bowling team',sorted(teams))
selected_city=st.selectbox("select the host city",sorted(cities))
target=st.number_input("Target score")
col3,col4,col5=st.columns(3)
with col3:
    current_score=st.number_input("Current score")
with col4:
    overs=st.number_input("Overs Completed")
with col5:
    wickets=st.number_input("Wickets out")
if st.button("Predict Probability"):
    balls_left= 120 - (overs*6)
    runs_left=target - current_score
    wickets=10 - wickets
    crr=current_score/overs
    rrr=(runs_left*6)/balls_left
    input_dataframe=pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],"city":[selected_city],
                              'runs_left':[runs_left],"balls_left":[balls_left],'wickets':[wickets],
                            "total_runs_x":[target],"crr":[crr],"rrr":[rrr]})
    
    # pipe.fit(input_dataframe)
    result=pipe.predict_proba(input_dataframe)

    loss=result[0][0]
    win=result[0][1]
    st.header(batting_team+"-"+str(round(win*100))+"%")
    st.header(bowling_team + "-" + str(round(loss * 100)) + "%")
    # remember use this version of scikit-learn == 1.3.1app
