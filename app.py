import streamlit as st
import pandas as pd
import os

# Function to check if the Excel file exists
def excel_file_exists():
    return os.path.exists('room_inspection.xlsx')

# Function to create the Excel file if it doesn't exist
def create_excel_file():
    dummy_data = {
        'Room Number': ['A001'],
        'General Condition': [False],
        'Furniture and Fixtures': [False],
        'Bathroom': [False],
        'Flooring': [False],
        'Walls and Ceilings': [False],
        'Electrical and Electronic Equipment': [False],
        'Safety and Security': [False],
        'Amenities': [False],
        'Cleanliness of Accessories': [False],
        'Room Ambiance': [False],
        'Guest Supplies': [False],
        'Special Requests': [False],
        'Final Checks': [False]
    }
    df = pd.DataFrame(dummy_data)
    df.to_excel('room_inspection.xlsx', index=False)

# Function to load data from the Excel file
def load_data():
    if not excel_file_exists():
        create_excel_file()
    return pd.read_excel('room_inspection.xlsx')

# Function to save data to the Excel file
def save_data(df):
    df.to_excel('room_inspection.xlsx', index=False)

# Main Streamlit app
st.title('Room Inspection Checklist')

# Sidebar with options
option = st.sidebar.selectbox('Select Room Number', ['Select Room Number'] + load_data()['Room Number'].tolist())

if option != 'Select Room Number':
    st.subheader(f'Room {option} Inspection Checklist')
    df = load_data()
    for column in df.columns[1:]:
        df.loc[df['Room Number'] == option, column] = st.checkbox(column, value=df[df['Room Number'] == option][column].iloc[0])

    # Save data when checkboxes are changed
    save_data(df)

# Add new room option
new_room_number = st.sidebar.text_input('Enter New Room Number')
if new_room_number:
    df = load_data()
    if st.sidebar.button('Add New Room'):
        if new_room_number not in df['Room Number'].tolist():
            new_room_data = {'Room Number': new_room_number}
            for column in df.columns[1:]:
                new_room_data[column] = False
            df = df.append(new_room_data, ignore_index=True)
            save_data(df)
            st.sidebar.success(f'Room {new_room_number} added successfully.')
            st.experimental_rerun()  # Reload the page to update dropdown options
        else:
            st.sidebar.warning(f'Room {new_room_number} already exists.')
