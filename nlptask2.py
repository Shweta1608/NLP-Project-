import pickle
import streamlit as st

# Load the machine learning model
pickle_in = open('classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)

def prediction(Status,location,bussiness_exe):
    # Convert the user input to numerical label
    if Status.lower() == 'interested':
        prediction_label = "Leads are going to convert"
    elif Status.lower() == 'not interested':
        prediction_label = "Leads are not going to convert"
    else:
        prediction_label = "Please provide valid input"

    return prediction_label

def main():
    st.title("Leads Prediction App")
    Status = st.text_input("Enter Status: ", "Type Here")
    location = st.text_input("Enter location: ", "Type Here")
    bussiness_exe = st.text_input("Enter comment: ", "Type Here")
    result = ""  # Initialize the result variable

    if st.button("Predict"):
        result = prediction(Status,location,bussiness_exe)
        st.write(result)

if __name__ == '__main__':
    main()
