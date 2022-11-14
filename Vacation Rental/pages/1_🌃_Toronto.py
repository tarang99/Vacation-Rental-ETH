

################################################################################
# Imports
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
from web3 import Web3
import requests



w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
################################################################################


# @TODO:
# From `crypto_wallet.py import the functions generate_account, get_balance,
#  and send_transaction
from crypto_wallet import generate_account, get_balance, send_transaction

################################################################################
# KryptoJobs2Go Candidate Information

# Database of KryptoJobs2Go candidates including their name, digital address, rating and hourly cost per Ether.
# A single Ether is currently valued at $1,500
candidate_database = {
    "15 Fitzgibbon Ave": [
        "15 Fitzgibbon Ave, Toronto, ON M1K 3Z7",
        "0xaC8eB8B2ed5C4a0fC41a84Ee4950F417f67029F0",
        "4.3",
        0.36,
        "Images/1.png",
        "Images/5.png",
        "Courtyard view : Garden view : Wifi : Dedicated workspace : Free parking on premises : HDTV : Washer – In building : Dryer – In building : Portable air conditioning",
        "Ameer Irfan",
        
    ],
    "66 Leahann Dr": [
        "66 Leahann Dr, Toronto, ON M1P 1B9",
        "0x269018DA9EE6ddEe7b889ec79138EEaBec7681Ed",
        "5.0",
        0.49 ,
        "Images/2.png",
        "Images/6.png",
        "Garden view : Public or shared beach access : Kitchen: Wifi : Free driveway parking on premises : Private hot tub – available all year : open specific hours : Pets allowed : Security cameras on property",
        "Tarang Patel",
    ],
    "7 Brimley Rd (Boat House)": [
        "7 Brimley Rd S #E-39, Toronto, ON M1M 3W3",
        "0x7D0746A7472AbEe96e2446F9ACa85Eb5FdF94eDB",
        "4.7",
        0.41,
        "Images/3.png",
        "Images/7.png",
        "Lake view : Beach access – Beachfront : Wifi – 10 Mbps : Dedicated workspace : Portable air conditioning : Private patio or balcony",
        "Maurice Le Gendre",
    ],
    "637 Lake Shore Blvd": [
        "637 Lake Shore Blvd W #631, Toronto, ON M5V 3J6",
        "0x5B51e64Df31EfB0EC90464906C00CB8522629d64",
        "4.1",
        0.25,
        "Images/4.png",
        "Images/8.png",
        "Lake View : Waterfront : Kitchen : Wifi : Free parking on premises : HDTV with Netflix : Elevator : Washer : Dryer : Security cameras on property",
        "Tejas Patel"
    
    ],
}


houses = ["15 Fitzgibbon Ave", "66 Leahann Dr", "7 Brimley Rd (Boat House)", "637 Lake Shore Blvd"]

with st.container():
    
    def get_house():
        """Display the database of KryptoJobs2Go candidate information."""
        db_list = list(candidate_database.values())

        for number in range(len(houses)):
            image_column, text_column = st.columns(2)
            with image_column:
                st.image(db_list[number][4], width=200)
                st.image(db_list[number][5], width=200)
            with text_column:
                st.write(" - **Location:** ", db_list[number][0])
                st.write(" - **Property Owner:** ", db_list[number][7])
                st.write(" - **Ethereum Account Address:** ", db_list[number][1])
                st.write(" - **Amenities -** ", db_list[number][6])
                st.write(" - **Customer Rating:** ", db_list[number][2])
                st.write(" - **Daily Rate per Ether:** ", db_list[number][3], "eth")
                st.text(" \n")
                st.write("___")
                

# Streamlit application headings
st.markdown("## Find The Best Vacation Rental Across Toronto!")
st.text(" \n")

################################################################################
# Streamlit Sidebar Code - Start

st.sidebar.markdown("## Client Account Address and Ethernet Balance in Ether")

##########################################
# customer’s (in this case, your) HD wallet and Ethereum account.

# @TODO:
#  Call the `generate_account` function and save it as the variable `account`
account = generate_account()

##########################################

# Write the client's Ethereum account address to the sidebar


##########################################

# @TODO
# Call `get_balance` function and pass it your account address
# Write the returned ether balance to the sidebar
ether_balance = get_balance(w3, account.address)
st.sidebar.write(ether_balance)

##########################################

# Create a select box to chose a FinTech Hire candidate
House = st.sidebar.selectbox("Select a House", houses)

# Create a input field to record the number of hours the candidate worked
with st.container():    
    hours = st.sidebar.number_input("Number of Days/Hours")
    check_in = st.sidebar.time_input("Check In Time")

    st.sidebar.markdown("## House Name, Number of Days, and Ethereum Address")

# Identify the FinTech Hire candidate
candidate = candidate_database[House][0]

# Write the house's name to the sidebar
st.sidebar.write(candidate)

# Identify the house's hourly rate
hourly_rate = candidate_database[House][3]

# Write the inTech Finder candidate's hourly rate to the sidebar
st.sidebar.write(hourly_rate)

# Identify the house owner's Ethereum Address
candidate_address = candidate_database[House][1]

# Write the inTech Finder candidate's Ethereum Address to the sidebar
st.sidebar.write(candidate_address)

# Write the house's name to the sidebar

st.sidebar.markdown("## Total in Ether")





daily_rate = candidate_database[House][3] * hours

# @TODO
# Write the `daily_rate` calculation to the Streamlit sidebar
st.sidebar.write(daily_rate)




if st.sidebar.button("Confirm Booking"):

    # @TODO
    # Call the `send_transaction` function and pass it 3 parameters:
    
    transaction_hash= send_transaction(w3,account, candidate_address, daily_rate)

    # Markdown for the transaction hash
    st.sidebar.markdown("#### Validated Transaction Hash")

    # Write the returned transaction hash to the screen
    st.sidebar.write(transaction_hash)

    # Celebrate your successful payment
    st.balloons()

# The function that starts the Streamlit application

get_house()

 # Contact       
with st.container():
    st.write("___")
    st.header("We are here to help!")
    st.write('##')

    # Contact Form
    contact_form = """
    <form action="https://formsubmit.co/YOUR@MAIL.COM" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

