#Core packages
import streamlit as st
from PIL import Image

#EDA packages
import pandas as pd
import numpy as np

#Data viz package
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")
import seaborn as sns

DATA_URL = ("Penguin data.csv")

#heading and info
st.markdown("# Self Exploratory Visualization on palmerpenguins")
st.markdown("Explore the dataset to know more about palmerpenguins")
img=Image.open('images/palmerpenguins.png')
st.image(img,width=100)
st.markdown("**Penguins** are some of the most recognizable and beloved birds in the world and even have their own holiday: **World Penguin Day is celebrated every year on April 25**. Penguins are also amazing birds because of their physical adaptations to survive in unusual climates and to live mostly at sea. Penguins propel themselves through water by flapping their flippers.  Bills tend to be long and thin in species that are primarily fish eaters, and shorter and stouter in those that mainly eat krill.”)st.markdown(“The data presented are of 3 different species of penguins - **Adelie, Chinstrap, and Gentoo,** collected from 3 islands in the **Palmer Archipelago, Antarctica.**")

#add button with image and effects
if st.button("Meet the Palmer Penguins"):
    img=Image.open('images/lter_penguins.png')
    st.image(img,width=700, caption="We are  Penguin 🐧")
    st.markdown("The data was collected and made available by **[Dr. Kristen Gorman](https://www.uaf.edu/cfos/people/faculty/detail/kristen-gorman.php)** and **[Palmer Station, Antarctica, LTER](https://pal.lternet.edu/)**.")
    images=Image.open('images/meet.png')
    st.image(images,width=600)

    #add effect: balloons
    st.balloons() 

#highlight data and add pictures
st.info("The dataset contains the different aspect between the species like Body Mass (g), Flipper Length (mm), Culmen Length (mm), Culmen Depth (mm) etc.")
img=Image.open('images/beak.jpg')
st.image(img,width=700)

#side panel and markdown with buttons
st.sidebar.markdown("## Side Panel")
st.sidebar.markdown("Use this panel to explore the dataset and create own viz.")

# Load  the Data 
def load_data(nrows):
    
    df = pd.read_csv(DATA_URL, nrows = nrows)
    lowercase = lambda x:str(x).lower()
    df.rename(lowercase, axis='columns',inplace=True)
    return df
st.markdown("### Click the button below to explore the dataset through my visualization.")
if st.button("Visualization created by Author "):
    img=Image.open('images/Palmer Penguins.png')
    st.image(img,width=700, caption="Viz. created by Author. 🐧")

    st.markdown(
    " **Takeaway:** Gento is *most massive & most gigantic* with an average body mass 5.08 Kg & average flipper length 217 mm.")
st.markdown("-----")
st.header("Now, Explore Yourself the Palmer Penguins")

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading palmerpenguins dataset...')

# Load 10,000 rows of data into the dataframe.
df = load_data(100000)

# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading palmerpenguins dataset...Completed!')
images=Image.open('images/meet.png')
st.image(images,width=600)

# Showing the original raw data
if st.checkbox("Show Raw Data", False):
    st.subheader('Raw data')
    st.write(df)

#showing the title
st.title('Quick  Explore')

#showing the subheading
st.sidebar.subheader('Quick  Explore')
st.markdown("Tick the box on the side panel to explore the dataset.")

#showing the checkbox
if st.sidebar.checkbox('Basic info'):

    #view raw data
    if st.sidebar.checkbox('Dataset Quick Look'):
        st.subheader('Dataset Quick Look:')

        #writing the output on screen
        st.write(df.head())
    if st.sidebar.checkbox("Show Columns"):
        st.subheader('Show Columns List')
        all_columns = df.columns.to_list()
        st.write(all_columns)
    if st.sidebar.checkbox('Statistical Description'):
        st.subheader('Statistical Data Descripition')
        st.write(df.describe())
    if st.sidebar.checkbox('Missing Values?'):
        st.subheader('Missing values')
        st.write(df.isnull().sum())

#create graphics
st.title('Create Own Visualization')
st.markdown("Tick the box on the side panel to create your own Visualization.")
st.sidebar.subheader('Create Own Visualization')
if st.sidebar.checkbox('Graphics'):

    #create count plot
    if st.sidebar.checkbox('Count Plot'):
        st.subheader('Count Plot')
        st.info("If error, please adjust column name on side panel.")
        column_count_plot = st.sidebar.selectbox("Choose a column to plot count. Try Selecting Sex ",df.columns)
        hue_opt = st.sidebar.selectbox("Optional categorical variables (countplot hue). Try Selecting Species ",df.columns.insert(0,None))
        fig = sns.countplot(x=column_count_plot,data=df,hue=hue_opt)
        st.pyplot()

    #create histogram/distplot
    if st.sidebar.checkbox('Histogram | Displot'):
        st.subheader('Histogram | Displot')
        st.info("If error, please adjust column name on side panel.")
        column_dist_plot = st.sidebar.selectbox("Optional categorical variables (countplot hue). Try Selecting Body Mass",df.columns)
        fig = sns.displot(df[column_dist_plot])
        st.pyplot()
            
    #create boxplot
    if st.sidebar.checkbox('Boxplot'):
        st.subheader('Boxplot')
        st.info("If error, please adjust column name on side panel.")
        column_box_plot_X = st.sidebar.selectbox("X (Choose a column). Try Selecting island:",df.columns.insert(0,None))
        column_box_plot_Y = st.sidebar.selectbox("Y (Choose a column - only numerical). Try Selecting Body Mass",df.columns)
        hue_box_opt = st.sidebar.selectbox("Optional categorical variables (boxplot hue)",df.columns.insert(0,None))
        # if st.checkbox('Plot Boxplot'):
        fig = sns.boxplot(x=column_box_plot_X, y=column_box_plot_Y,data=df,palette="Set3")
        st.pyplot()

st.markdown("# Inspire Yourself")        
if st.button("Viz by Tableau Community"):
    img=Image.open('images/D1.png')
    st.subheader("Viz by [Scott Renfree-Tuck](https://public.tableau.com/profile/scott.renfree.tuck#!/vizhome/MakeoverMondayW282020-PalmersPenguins/Dashboard2)")
    st.image(img,width=950)
    st.subheader("Viz by  [Agata Ketterick](https://public.tableau.com/profile/agata1619#!/vizhome/PalmerPenguinsMakeoverMonday2020_28/Penguins)")
    img2=Image.open('images/D2.png')
    st.image(img2,width=950)
    img3=Image.open('images/D3.png')
    st.subheader("Viz by [Swati Dave](https://public.tableau.com/profile/swati.dave#!/vizhome/PenguinParadox/PenguinStory)")
    st.image(img3,width=950)
st.markdown(" > Thank you for exploring palmerpenguins. This is my first Streamlit work. Feedbacks are highly welcomed.")

#adding data source info and artwork acknowledgement
st.sidebar.markdown("[Data Source](https://data.world/makeovermonday/2020w28)")
st.sidebar.info(" [Source Article](https://github.com/allisonhorst/palmerpenguins) | [Twitter  Tags](https://twitter.com/allison_horst/status/1270046399418138625)")
st.sidebar.info("Artwork by [Allison Horst](https://twitter.com/allison_horst) ")
st.sidebar.info("Self Exploratory Visualization on palmerpenguins - Brought To you By [Mala Deep](https://github.com/maladeep)  ")
st.sidebar.text("Built with  ❤  Streamlit")

