import pickle
import streamlit as st

# Load the machine learning model
pickle_in = open('classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)

def prediction(Status):
    # Convert the user input to numerical label
    if Status.lower() == 'interested':
        prediction_label = "Leads are going to convert"
    elif Status.lower() == 'not interested':
        prediction_label = "Leads are not going to convert"
    else:
        prediction_label = "You entered something else."

    return prediction_label

def main():
    st.title("Leads Prediction App")
    Status = st.text_input("Enter Status: ", "Type Here")
    result = ""  # Initialize the result variable

    if st.button("Predict"):
        result = prediction(Status)
        st.write(result)

if __name__ == '__main__':
    main()
