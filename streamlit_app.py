import streamlit
import pandas
streamlit.title('Test Streamlit');
streamlit.header('Is it working?');
streamlit.text('It is working fine');
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
