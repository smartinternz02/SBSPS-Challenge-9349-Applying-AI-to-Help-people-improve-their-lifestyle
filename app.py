#importing all the important libraries
from ast import Break
import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

#building the sidebar of the web app which will help us navigate through the different sections of the entire application

#Home Page 
dictionary = {'Home': ['Home'], 'Health Analyser': ['Covid-19', 'Diabetes' , 'Heart Disease'] ,'Plots Page': ['Plots'], 'Lifestyle Analyser':['lifestyle Tracker']}

Navigation = st.sidebar.selectbox("Navigation Menu:", sorted(dictionary.keys()))
rad = st.sidebar.radio("Choose any page:", sorted(dictionary[Navigation]))


#displays all the available disease prediction options in the web app
if rad=="Home":
    st.title("RYLO LIFESTYLE AI")
    st.subheader("Raising Youth's Lifestyle Optimizer")
    st.image("images/Lifestyle-home.png")
    user = st.text_input('Enter your Name')
    role = st.selectbox("Select your Role: ", ['School Student', 'College Student', 'Employee','Senior Citizen'])
    age = st.slider("Select your age", 10, 70)
    if st.button('Submit'):
        st.write('Hi', user ,'Welcome to RYLO Lifestyle AI')
        st.write(user ,'Your role is', role)
        st.write(user ,'Your age is = {}'.format(age))
    else:
        st.write('Hi Welcome to RYLO Lifestyle AI')
        
    col1, col2 = st.columns(2)

    with col1:
        st.write(user,'Please click on the routine button to get your routines')

    with col2:
       routine = st.button('Routine')
        
    if routine:
    
        if (age < 18):
            st.subheader('1.Wake up early')
            routine1=st.image('images/wakeup.jpg')
        
            st.subheader('2.Eat a healthy Breakfast')
            routine2=st.image('images/breakfast.jpg')
            
            st.subheader('3.Meditation')
            routine3=st.image('images/meditation.jpg')
            
            st.subheader('4.Sleep on time')
            routine4=st.image('images/sleep.jpg')
            
            st.success("You have not completed your routine")
            
        elif (age >= 18 and age < 29):
            
            st.subheader('1.Raise Early')
            task1=st.image("images/raise_early.jpg")
            
    
            st.subheader('2.Start Your day with Affrimation')
            task2=st.image("images/Affirmations.jpeg")
            
            st.subheader('3.Workout')
            task3=st.image("images/workout.jpg")
            
            st.subheader('4.Do not skip Breakfast')
            task4=st.image("images/breakfast.jpg")
            
             
            st.subheader('5.Be mindful of your social media usage')
            task5=st.image("images/socialmedia.png")
            
            st.success("Congrats you have sucessfully completed your routine")
            
            
        elif (age >= 29 and age < 50):
            st.subheader('1.Seize the day early')
            rem1=st.image("images/seizeday.jpg")
            
           
            st.subheader('2.Take your Vitamins')
            rem2=st.image("images/thoughts.jpg")
           
            st.subheader('3.Fruits and Vegetables = Priority')
            rem3=st.image("images/fruits&veg.jpg")
            
            st.subheader('4.Engage your core')
            rem4=st.image("images/engagecore.png")
           
            st.subheader('5.Nap and do not feel bad about it')
            rem5=st.image("images/nap.jpg")
            
            st.success("Congrats you have sucessfully completed your routine")
           
            
        elif (age >= 50 and age < 71):
            st.subheader('1.Watch the Sunset and Sunshine')
            date1=st.image("images/sunrise&set.jpg")
            
           
            st.subheader('2.Stay Hydrated')
            date2=st.image("images/hydrate.png")
           
            st.subheader('3.Take your Supplements')
            date3=st.image("images/supplement.jpg")
            
            st.subheader('4.Have dietry regimen')
            date4=st.image("images/regimen.jpg")
            
            st.subheader('5.Journal out unhappy thoughts')
            date5=st.image("images/journalout.jpg")
           
            st.subheader('6.Get enough Sleep')
            date1=st.image("images/enoughsleep.jpg")
            
            st.success("Congrats you have sucessfully completed your routine")
           
        else:
            st.write('Your age is out of the specified range')
            
    else:
        st.write('Click on the routine button')
        
if rad == "lifestyle Tracker":
    st.title("RYLO Lifestyle Analyser")
    st.subheader("Answer the following questions to examine your lifestyle")
    
    st.subheader("1.How much did you eat today?")
    st.text("select from range low=1 medium=2 high=3")
    eat = st.slider("select an option for question 1",1,3)
    
    st.subheader("2.how much did you sleep")
    sleep = st.selectbox("select an option for question 2",['6-8 Hours','4-6 Hours','2-4 HOurs'])
    
    st.subheader("3.What mood where you in ?")
    mood = st.radio("select an option for question 3",('very good ', 'Normal', 'Bad'))
    
    st.subheader("4.how  energized did you feel")
    st.text("select from range low=1 medium=2 high=3")
    energy = st.slider("select an option for question 4",1,3)
    
    st.subheader("5.Did you eat healthy?")
    health1 = st.radio("select an option for question 5",('Yes', 'No'))
    if health1 == 'Yes':
          health = 1
    else:
        health = 0
    
    st.subheader("6.Did you exercise today?")
    exercise1 = st.radio("select an option for question 6",('Yes', 'No'))
    if exercise1 == 'Yes':
          exercise = 1
    else:
        exercise = 0
    
    st.subheader("7.Are you done with with your meditation?")
    meditation1 = st.radio("select an option for question 7",('Yes', 'No'))
    if meditation1 == 'Yes':
          meditation = 1
    else:
        meditation = 0
    
    st.subheader("8.Do you Love yourself?")
    love1 = st.radio("select an option for question 8",('Yes', 'No'))
    if love1 == 'Yes':
          love = 1
    else:
        love = 0
        
    
    st.subheader("9.Are you Worring about others")
    worry1 = st.radio("select an option for question 9",('Yes', 'No'))
    if worry1 == 'Yes':
          worry = 1
    else:
        worry = 0
    
    if st.button('Submit'):
        result= worry+love+meditation+exercise+health+energy+eat
        st.write("Your toatal score is ",result)

        
        if (result<=4):
            
            st.subheader("you sould maintain self confidence")
            st.warning("Self Confidence")
        
        elif (result >=4 and result <8):
            
            st.subheader("you sould remain self confidence")
            st.info("Calm and Stable")
            
        else:
            
            st.subheader("you are fair and equitable")
            st.success("Good to go")
        
        
            
            
    
    

#Covid-19 Prediction

#loading the Covid-19 dataset
df1=pd.read_csv("Covid-19 Predictions.csv")
#cleaning the data by dropping unneccessary column and dividing the data as features(x1) & target(y1)
x1=df1.drop("Infected with Covid19",axis=1)
x1=np.array(x1)
y1=pd.DataFrame(df1["Infected with Covid19"])
y1=np.array(y1)
#performing train-test split on the data
x1_train,x1_test,y1_train,y1_test=train_test_split(x1,y1,test_size=0.2,random_state=0)
#creating an object for the model for further usage
model1=RandomForestClassifier()
#fitting the model with train data (x1_train & y1_train)
model1.fit(x1_train,y1_train)

#Covid-19 Page

#heading over to the Covid-19 section
if rad=="Covid-19":
    st.header("Know If You Are Affected By Covid-19")
    st.write("All The Values Should Be In Range Mentioned")
    #taking the 4 most important features as input as features -> Dry Cough (drycough), Fever (fever), Sore Throat (sorethroat), Breathing Problem (breathingprob)
    #a min value (min_value) & max value (max_value) range is set so that user can enter value within that range
    #incase user enters a value which is not in the range then the value will not be taken whereas an alert message will pop up
    drycough=st.number_input("Rate Of Dry Cough (0-20)",min_value=0,max_value=20,step=1)
    fever=st.number_input("Rate Of Fever (0-20)",min_value=0,max_value=20,step=1)
    sorethroat=st.number_input("Rate Of Sore Throat (0-20)",min_value=0,max_value=20,step=1)
    breathingprob=st.number_input("Rate Of Breathing Problem (0-20)",min_value=0,max_value=20,step=1)
    #the variable prediction1 predicts by the health state by passing the 4 features to the model
    prediction1=model1.predict([[drycough,fever,sorethroat,breathingprob]])[0]
    
    #prediction part predicts whether the person is affected by Covid-19 or not by the help of features taken as input
    #on the basis of prediction the results are displayed
    if st.button("Predict"):
        if prediction1=="Yes":
            st.warning("You Might Be Affected By Covid-19")
        elif prediction1=="No":
            st.success("You Are Safe")

#Diabetes Prediction

#loading the Diabetes dataset
df2=pd.read_csv("Diabetes Predictions.csv")
#cleaning the data by dropping unneccessary column and dividing the data as features(x2) & target(y2)
x2=df2.iloc[:,[1,4,5,7]].values
x2=np.array(x2)
y2=y2=df2.iloc[:,[-1]].values
y2=np.array(y2)
#performing train-test split on the data
x2_train,x2_test,y2_train,y2_test=train_test_split(x2,y2,test_size=0.2,random_state=0)
#creating an object for the model for further usage
model2=RandomForestClassifier()
#fitting the model with train data (x2_train & y2_train)
model2.fit(x2_train,y2_train)

#Diabetes Page

#heading over to the Diabetes section
if rad=="Diabetes":
    st.header("Know If You Are Affected By Diabetes")
    st.write("All The Values Should Be In Range Mentioned")
    #taking the 4 most important features as input as features -> Glucose (glucose), Insulin (insulin), Body Mass Index-BMI (bmi), Age (age)
    #a min value (min_value) & max value (max_value) range is set so that user can enter value within that range
    #incase user enters a value which is not in the range then the value will not be taken whereas an alert message will pop up
    glucose=st.number_input("Enter Your Glucose Level (0-200)",min_value=0,max_value=200,step=1)
    insulin=st.number_input("Enter Your Insulin Level In Body (0-850)",min_value=0,max_value=850,step=1)
    bmi=st.number_input("Enter Your Body Mass Index/BMI Value (0-70)",min_value=0,max_value=70,step=1)
    age=st.number_input("Enter Your Age (20-80)",min_value=20,max_value=80,step=1)
    #the variable prediction1 predicts by the health state by passing the 4 features to the model
    prediction2=model2.predict([[glucose,insulin,bmi,age]])[0]
    
    #prediction part predicts whether the person is affected by Diabetes or not by the help of features taken as input
    #on the basis of prediction the results are displayed
    if st.button("Predict"):
        if prediction2==1:
            st.warning("You Might Be Affected By Diabetes")
        elif prediction2==0:
            st.success("You Are Safe")

#Heart Disease Prediction

#loading the Heart Disease dataset
df3=pd.read_csv("Heart Disease Predictions.csv")
#cleaning the data by dropping unneccessary column and dividing the data as features(x3) & target(y3)
x3=df3.iloc[:,[2,3,4,7]].values
x3=np.array(x3)
y3=y3=df3.iloc[:,[-1]].values
y3=np.array(y3)
#performing train-test split on the data
x3_train,x3_test,y3_train,y3_test=train_test_split(x3,y3,test_size=0.2,random_state=0)
#creating an object for the model for further usage
model3=RandomForestClassifier()
#fitting the model with train data (x3_train & y3_train)
model3.fit(x3_train,y3_train)

#Heart Disease Page

#heading over to the Heart Disease section
if rad=="Heart Disease":
    st.header("Know If You Are Affected By Heart Disease")
    st.write("All The Values Should Be In Range Mentioned")
    #taking the 4 most important features as input as features -> Chest Pain (chestpain), Blood Pressure-BP (bp), Cholestrol (cholestrol), Maximum HR (maxhr)
    #a min value (min_value) & max value (max_value) range is set so that user can enter value within that range
    #incase user enters a value which is not in the range then the value will not be taken whereas an alert message will pop up
    chestpain=st.number_input("Rate Your Chest Pain (1-4)",min_value=1,max_value=4,step=1)
    bp=st.number_input("Enter Your Blood Pressure Rate (95-200)",min_value=95,max_value=200,step=1)
    cholestrol=st.number_input("Enter Your Cholestrol Level Value (125-565)",min_value=125,max_value=565,step=1)
    maxhr=st.number_input("Enter You Maximum Heart Rate (70-200)",min_value=70,max_value=200,step=1)
    #the variable prediction1 predicts by the health state by passing the 4 features to the model
    prediction3=model3.predict([[chestpain,bp,cholestrol,maxhr]])[0]
    
    #prediction part predicts whether the person is affected by Heart Disease or not by the help of features taken as input
    #on the basis of prediction the results are displayed
    if st.button("Predict"):
        if str(prediction3)=="Presence":
            st.warning("You Might Be Affected By Diabetes")
        elif str(prediction3)=="Absence":
            st.success("You Are Safe")
                                        
#Plots Page

#heading over to the plots section
#plots are displayed for each disease prediction section 
if rad=="Plots":
    #
    type=st.selectbox("Which Plot Do You Want To See?",["Covid-19","Diabetes","Heart Disease"])
    if type=="Covid-19":
        fig=px.scatter(df1,x="Difficulty in breathing",y="Infected with Covid19")
        st.plotly_chart(fig)

    elif type=="Diabetes":
        fig=px.scatter(df2,x="Glucose",y="Outcome")
        st.plotly_chart(fig)
    elif type=="Heart Disease":
        fig=px.scatter(df3,x="BP",y="Heart Disease")
        st.plotly_chart(fig)
