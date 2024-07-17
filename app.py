import streamlit as st
import pandas as pd

# Load data from CSV
@st.cache_data  # Cache data for better performance
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

def main():
    st.title('Bus Data Filtering App')
    
    # Load data
    file_path = r"C:\Users\jeeva\OneDrive\Desktop\New folder\Project1_capstone\final_redbus.csv"
    df = load_data(file_path)
    
    # Sidebar filter by bus type
    bus_type = st.sidebar.multiselect('Bus Type', options=df['type'].unique())
    # Filter data based on selected bus types
    filtered_data = df[df['type'].isin(bus_type)]


    Route = st.sidebar.multiselect('Route', options=df['route-collected'].unique())
    # Filter data based on selected bus routes
    filtered_data = df[df['route-collected'].isin(Route)]
    

    bus_name = st.sidebar.multiselect('Bus Name', options=df['name'].unique())
    # Filter data based on selected bus name
    filtered_data = df[df['name'].isin(bus_name)]


    departing_time = st.sidebar.multiselect('Departing Time', options=df['departure_time'].unique())
    # Filter data based on selected departing time
    filtered_data = df[df['departure_time'].isin(departing_time)]


    reaching_time = st.sidebar.multiselect('Arrival Time', options=df['arrival_time'].unique())
    # Filter data based on selected departing time
    filtered_data = df[df['arrival_time'].isin(reaching_time)]


    ticket_price = st.sidebar.multiselect('Ticket Price', options=df['price'].unique())
    # Filter data based on selected departing time
    filtered_data = df[df['price'].isin(ticket_price)]

    seats = st.sidebar.multiselect('Seats Availability', options=df['seats_available'].unique())
    # Filter data based on selected departing time
    filtered_data = df[df['seats_available'].isin(seats)]

    rating = st.sidebar.multiselect('Star Rating', options=df['rating'].unique())
    # Filter data based on selected departing time
    filtered_data = df[df['rating'].isin(rating)]


    # Display filtered data
    st.write('Filtered Data:')
    st.write(filtered_data)

if __name__ == '__main__':
    main()
