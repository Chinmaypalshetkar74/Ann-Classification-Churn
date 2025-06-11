import streamlit as st 
import numpy as np 
import tensorflow as tf 
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
import pandas as pd 
import pickle

# Load train model 
model = tf.keras.models.load_model('model.h5')

# Load the encoders and scaler 
with open('label_encoder_gender.pkl', 'rb') as file:
    label_encoder_gender = pickle.load(file)

with open('OneHot_Encoder_geo.pkl', 'rb') as file:
    OneHot_Encoder_geo = pickle.load(file)

with open('scaler.pkl','rb') as file:
    scaler = pickle.load(file)


##stremlit app 
st.title('Customer Churn Prediction')

#user inputs 
geography = st.selectbox('Geography' ,OneHot_Encoder_geo.categories_[0])
gender = st.selectbox('Gender',label_encoder_gender.classes_)
age = st.slider('Age', 18,92)
balance = st.number_input('Balance')
credit_score = st.number_input('Credit Score')
estimated_salary =st.number_input('Estimated Salary')
tenure= st.slider('Tenure', 0,10)
num_of_products = st.slider('Number of product',1, 4)
has_cr_card = st.selectbox('Has credit Card', [0,1])
is_active_number = st.selectbox('Is Active Member',[0,1])

#prepare the input_data

#Example input data 

input_data = {
    'CreditScore': [credit_score],
    'Gender': [label_encoder_gender.transform([gender])[0]],
    'Age': [age],
    'Tenure': [tenure],
    'Balance': [balance],
    'NumOfProducts': [num_of_products],
    'HasCrCard': [has_cr_card],
    'IsActiveMember': [is_active_number],
    'EstimatedSalary' : [estimated_salary]
    
    
}

#one hot encoder 'Geography'
#one hot Encode 'Geography'
geo_encoder= OneHot_Encoder_geo.transform([[geography]]).toarray()
geo_encoder_df = pd.DataFrame(geo_encoder, columns=OneHot_Encoder_geo.get_feature_names_out(['Geography']))
geo_encoder_df

#combine with input data  
input_data = pd.DataFrame(input_data)# Convert dict to DataFrame
input_data = pd.concat([input_data.reset_index(drop=True), geo_encoder_df], axis=1)

#scaled input data
input_data_scaled = scaler.transform(input_data)

#predict churn 

prediction = model.predict(input_data_scaled)
prediction_proba = prediction[0][0]

st.write(f'Churn Probability:{prediction_proba:.2f}')
if prediction_proba > 0.5:
    st.write('The Customer is like to churn.')
else:
    st.write('the Customer is not likely to churn.')

