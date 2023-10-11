import base64
import streamlit as st
from PIL import Image
from streamlit_extras.mention import mention


# page_config is what is seen in broswer tab
st.set_page_config(
    page_title="Projects",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"   # use'auto' for first visit
)

#----Resources---
startup_prj_img =Image.open('images/startup-india.jpg')
heat_img = Image.open('images/HeatMap.png')
categories_img = Image.open('images/Top_Categories.png')
images=[heat_img,categories_img]

link_img=Image.open('images/Linkedin.png')
#---------------------------------------------------------------
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('images/bg.jpg') 

#----------------------sidebar---------------------------



# ------------------------------------------------------------------------

def local_css(file_name):    #import local machine css file
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ------------------------------------------------------------------------
st.header("Projects Portfolio")
st.write("***")  ## adding a horiizontal line
#-------------------------------project 1--------------------------------
with st.container():
    text_column, image_column = st.columns((3,1))
    with text_column:
        st.subheader("Startupindia.gov.in ETL+EDA project")
        st.write("*Indian registered startups under Startup India Campaign*")
        st.markdown("""
            - Utilised snscrape to scrape tweets from top blockchain websites such as CoinGecko and CoinMarketCap
            - Built webscraper using BeautifulSoup4 to scrape content from fintech news websites such as https://blockchain.news
            """)
        mention(label="Github Repo", icon="github", url="https://github.com/dhirajmahato/webscrapping",)
    with image_column:
        with st.container():
                left, right = st.columns((1,1))
                with left:
                    st.image(heat_img)
                with right:
                     st.image(categories_img)
#--------------------project 1--------------------------------
with st.container():
    text_column, image_column = st.columns((3,1))
    with text_column:
        st.subheader("Linkedin Job Data Analysis")
        st.write("*Scraping Job posting and required skillsets respectively*")
        st.markdown("""
            - Utilised snscrape to scrape tweets from top blockchain websites such as CoinGecko and CoinMarketCap
            - Built webscraper using BeautifulSoup4 to scrape content from fintech news websites such as https://blockchain.news
            """)
        mention(label="Streamlit App", icon="streamlit", url="https://huggingface.co/spaces/harrychangjr/tiktok_analytics",)
        mention(label="Github Repo", icon="github", url="https://github.com/dhirajmahato/webscrapping",)
    with image_column:
        st.image(link_img)


# adding some styles from local machine via function defined above
local_css("css/styles.css") #  To get rid of the Streamlit branding stuff @ lower left page

