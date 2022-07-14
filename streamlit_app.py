import streamlit
import pandas
streamlit.title('Test Streamlit');
streamlit.header('Is it working?');
streamlit.text('It is working fine');
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlist.multiselect("Pick some fruits:",list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list) 
