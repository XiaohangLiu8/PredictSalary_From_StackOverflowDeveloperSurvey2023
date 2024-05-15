import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

regressor = data['model']
le_country = data['le_country']
le_mainbranch = data['le_mainbranch']
le_age = data['le_age']
le_edlevel = data['le_edlevel']

def show_predict_page():
    st.title("Software Developer Salary Prediction")

    st.write("""### We need some information to predict the salary""")

    countries = (
        "United States of America"                   ,
        "Germany"                                              ,
        "United Kingdom of Great Britain and Northern Ireland" ,
        "India"                                          ,
        "Canada"                                          ,
        "France"                                          ,
        "Poland"                                          ,
        "Brazil"                                          ,
        "Netherlands"                                          ,
        "Australia"                                          ,
        "Spain"                                          ,
        "Italy"                                          ,
        "Sweden"                                          ,
        "Switzerland"                                          ,
    )

    mainbranch = (
        'I am a developer by profession',
        'I am not primarily a developer, but I write code sometimes as part of my work/studies'
    )

    age = (
        'Under 18 years old',
        '18-24 years old', 
        '25-34 years old',
        '35-44 years old',
        '45-54 years old', 
        '55-64 years old', 
        '65 years or older',
        'Prefer not to say'
    )

    education = (
        "Less than a Bachelors", 
        "Bachelor’s degree", 
        "Master’s degree",
        "Professional degree"
    )

    country = st.selectbox("Country", countries)
    mainbranch = st.selectbox("Which of the following options best describes you today?", mainbranch)
    age = st.selectbox("What is your age?", age)
    education = st.selectbox("Education Level", education)

    experience = st.slider("Years of Experience", 0, 50, 3)

    ok = st.button("Calculate Salary")
    if ok:
        data = np.array([[country, mainbranch, age, education, experience]])
        data[:, 0] = le_country.transform(data[:, 0])
        data[:, 1] = le_mainbranch.transform(data[:, 1])
        data[:, 2] = le_age.transform(data[:, 2])
        data[:, 3] = le_edlevel.transform(data[:, 3])

        salary = regressor.predict(data)
        print(salary)
        st.subheader(f"The estimated salary is ${salary[0]:.2f}")

        