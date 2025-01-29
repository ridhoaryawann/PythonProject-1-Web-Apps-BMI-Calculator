#### BMI Calculator

# This syntax build a **web app** for calculating Body Mass Index
# This syntax is build to learn essential function of **python** and **streamlit**

# Import Library
import streamlit as st
import pandas as pd 

# Set the title
st.title("Body Mass Index Calculator")

# Built input function & variable to store data
height = st.number_input(label="Enter your height in cm", 
                        min_value = 70.01,
                        max_value = 250.01,
                        step = 1., 
                        format = "%.2f"
                        )
weight = st.number_input(label="Enter your weight in kg", 
                        min_value = 40.00,
                        max_value = 250.00,
                        step = 1., 
                        format = "%.2f"
                        )

# Build function to process variable
def BMI( height, weight):

    bmi = round( weight / ( ( height / 100 ) ** 2 ) , 2 )

    if bmi < 16:
        return bmi, "severely underweight"

    elif bmi >= 16 and bmi < 18.5:
        return bmi, "underweight"

    elif bmi >= 18.5 and bmi < 25:
        return bmi, "normal & healthy"

    elif bmi >= 25 and bmi < 30:
        return bmi, "overweight"

    elif bmi >= 30 and bmi < 35:
        return bmi, "obese class 1"

    elif bmi >= 35 and bmi < 40:
        return bmi, "obese class 2"

    else:
        return bmi, "obese class 3"


# 1. Applied the function
# 2. Build variable to save data point that comes out from function
bmi, quote = BMI( height, weight )
st.write(f"your height is: {height}")
st.write(f"your weight is: {weight}")
st.write("your bmi is: {} and you are: '{}' ".format( bmi, quote ) )


# Create a reference for bmi information
import pandas as pd

data = {'Body Mass' : ['<16','16-18.5','18.5-25','25-30','30-35','35-40','>40'],
        'Category' : ['Severely underweight','Underweight','Healthy','Overweight','Obese Class 1','Obese Class 2','Obese Class 1']}

df = pd.DataFrame(data)

# Create table for web app
st.write('Body Mass Index Table Reference')
st.table(df)
