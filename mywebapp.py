#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 12:13:43 2022

@author: venkatakrishnasunkara
"""
import streamlit as st
import pandas as pd 
from gspread_pandas import Spread,Client
from google.oauth2 import service_account
import pubchempy as pcp
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = service_account.Credentials.from_service_account_info(
                st.secrets["gcp_service_account"], scopes = scope)
client = Client(scope=scope,creds=credentials)
spreadsheetname = "Database"
spread = Spread(spreadsheetname,client = client)
st.write(spread.url)

sh = client.open(spreadsheetname)
worksheet_list = sh.worksheets()

st.write(spread.url)
df = pd.DataFrame()


st.set_page_config(page_title ="Mycolorado", page_icon=":tada:", layout = "wide")
st.image('mc.png')


# subheader 
st.subheader("Welcome to Mycolorado, the place where your opoinions matter")
st.write("Your views and opinions matter to us.") 
st.write("The governament values your input regarding the rules and regulations that govern the businesses in colorado ")
st.write("[learn More>](hhttps://leg.colorado.gov/bills/hb21-1230)")


#----- add an annimmation for the webpage. using lottie files
#with st.container():
   

firstname = st.text_input("Enter your First name","")
lastname = st.text_input("Enter your last name","")


age = st.number_input("Enter your age",min_value=0, max_value=100 , step=1)
address = st.text_area("Enter your address")
check= st.checkbox("Click if your residential address is your mailing address")
if  check:
    st.write("Thank you")
else:
    mailing_address = st.text_area("ENTER YOUR MAILING ADDRESS")

dob = st.date_input("Enter your DOB")
CID = st.text_input("Enter your CID",max_chars=4)
email = st.text_input("Enter your email address")
mobile = st.number_input("Enter your mobile number ", min_value = 0, max_value=10, step = 1)
coresident = st.selectbox("Seclect if you are a resident", ['Yes', 'No'])
#if coresident == "No":
    
weight = st.number_input("Please enter your weight", min_value = 0, max_value=(3))
Haircolor = st.text_input(("Enter your haircolor"))
zzip = st.number_input("ZIP", min_value = 5)
city = st.text_input("Enter your city name")
state = st.text_input("State")
if state != "colorado" or state != "Colorado":
    st.write("You have to be a coloradian to access this form")
    
    
    
    

expiration = st.date_input("Enter your expiration date")
SEX = st.selectbox("Enter your sex", ["M", "F","N"])
Race =st.selectbox("Selct your race",["Other","White", "Black or African American", "American Indian or Alaska Native", "Asian", "Native Hawaiian or Other Pacific Islander"])
height = st.number_input("Please enter your height in inches")
Eyecolor = st.text_input("Please enter your Eyecolor")
Organ = st.selectbox(("Are you a organ donor"), ["Yes","No"])
vehicleclass= st.text_input("Enter your vehicle classification")
vechicle_licence = st.text_input("Enter your vechicles Licence Plate Number")
Insurance = st.file_uploader("Enter your vechicle Isurance Number", type = ['pdf'])
vechicle_registration = st.file_uploader("Please upload your vechicle registration", type=['pdf'])
Drivers_class = st.selectbox(("Select your drivers licence class"), ["D","JD","A,B,C","E","M"])
#L_data = 
Image =st.file_uploader("Please upload your image", type=["jpg",'jpeg','png']) 
merchat_key = st.text_input("Enter Merchant Primary Key")
merchant_comp = st.text_input("Enter Merchant Company Name")


public_gsheets_url = "https://docs.google.com/spreadsheets/d/1ACI_3JD4xLePKP3wMBGjeq8f83f3vWudLkhW-LUaBcw/edit?usp=sharing"

df = df.append(age)



if firstname !="":
    
    st.markdown(
    f"""
    *First Name :{firstname}
    *Last Name :{lastname}
    *Age:{age}
"""
)
