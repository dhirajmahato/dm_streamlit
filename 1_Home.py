import json
import base64
import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components

# page_config is what is seen in broswer tab
st.set_page_config(
    page_title="Dhiraj Mahato",
    page_icon="boy",
    layout="wide",
    initial_sidebar_state="collapsed"   # use'auto' for first visit
)

# Define custom CSS to set the SVG as background
custom_css1 = f"""
<style>
  .stApp {{
        background-image: url('https://cdn.svgator.com/images/2022/06/animated-svg-background-css.svg');
        background-size: cover;
    }}
</style>
"""

# Display the custom CSS with the SVG background
st.markdown(custom_css1, unsafe_allow_html=True)


#----------------------Resource-----------------
profile_img = Image.open('images/boy.png')
exp_img = Image.open('images/code.png')
computing_img=Image.open('images/cloud-computing.png')

prj_ims =[]
start_img=Image.open('images/startup.png')
iit_img=Image.open('images/iit.png')
spot_img=Image.open('images/Spotify.png')
link_img=Image.open('images/Linkedin.png')

indus_imgs= ['images/wipro.png', 'images/Tata_Steel_Logo.svg']
wipro_img=Image.open('images/wipro.png')
Tata_img=Image.open('images/Tata_Steel_Logo.svg')


# -----------------------Sidebar----------------------


# -----------------------------Some Functions definition to be used later --------------------------------------------------------
def local_css(file_name):    #import local machine css file
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# --------------------------------Home_Page content--------------------------------------------
# Your Streamlit app content goes here
st.markdown("<h2 style='text-align: center;'>DHIRAJ MAHATO</h2>", unsafe_allow_html=True)

selected = option_menu(
            menu_title=None,  # required
            options=["About Me", "Experience", "Data Stack"],  # required
            icons=["house", "list-task", "wrench"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional i.e phela tab kaha rahega
            orientation="horizontal",
            styles={
                "container": {"padding": "0!important", "background-color": "#fafafa"},
                "icon": {"color": "black", "font-size": "20px"},
                "nav-link": {
                    "font-size": "15px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#eee",
                },
                "nav-link-selected": {"background-color": "skyblue"},
            }
        )
# ------------------------About Me----------------------------------

if selected == "About Me":
    with st.container():
            left_column, right_column = st.columns((2.5, 1))
            with left_column:
                st.markdown("#### Data Alchemist | Tech Enthusiast | Innovation Catalyst")
                st.write("👋🏻 Hi, I'm a data enthusiast, passionate about simplifying complex challenges with data-driven solutions, based in Bengaluru, India.")
                st.write("👨🏼‍💻 **Interest Areas**: Data Visualization, Market Basket Analysis, Recommendation Systems, Natural Language Processing")
                st.write("""💭 In my *data odyssey*, I have gained expertise in:
- Leveraging emerging technologies like **LLMs** and **serverless computing** to optimize data pipelines and infrastructure for maximum efficiency.
- Crafting data-driven models unlocking hidden patterns and trends.""")
                st.write("🏋🏻 In addition, I like to exercise in the gym, listening music and... enjoy cooking & eating good food in my free time!")
                st.write ("")
                #st.write("📄 [Resume (1 page)](https://drive.google.com/file/d/164EEVH6BmvC89q2M4WsBNF1JyddDAbNY/view?usp=sharing)")
            
            with right_column:
                st.markdown("")
                st.markdown("")
                #st.image(profile_img, caption='', width=250)
                components.html(
                """
                <script src="https://unpkg.com/@dotlottie/player-component@latest/dist/dotlottie-player.mjs" type="module"></script>
                <dotlottie-player src="https://lottie.host/7ccfbb84-c9a4-450e-a0a7-7009d76a6318/nHzB0MdtaP.json" background="transparent" speed="1" style="width: 300px; height: 300px" direction="1" mode="normal" loop autoplay></dotlottie-player>
                """,
                height=300,
                ) 


            
# ---------------------------------------Experience ----------------------------------------------------------
if selected == "Experience":
    with st.container():
        st.write(
                """
🌍 **Global Impact**: My journey traverses industries, from finance to healthcare to e-commerce, leaving a trail of data-driven successes.
                """)
        col1, col2 = st.columns((1,1))
        with col1:
            st.subheader("Projects")
            with st.container():   #first row of projects
                left, mid, right = st.columns((1,1,1))
                with left:
                    st.image(start_img, caption='', width=150)
                with mid:
                    st.image(spot_img, caption='', width=150)
                with right:
                     st.image(iit_img, caption='', width=100)


            with st.container(): # second row of projects
                left, mid, right = st.columns((1,1,1))
                with left:
                    st.image(link_img, caption='', width=150)
                with mid:
                    st.image(spot_img, caption='', width=150)
                with right:
                     st.image(iit_img, caption='', width=100)


            st.write(
                """
                visit Projects page for more details
                """
            )
            

        with col2:
            st.subheader("Industry")
            
            with st.container():
                left, right = st.columns((1,1))
                with left:
                    st.image(wipro_img, caption='', width=150)
                with right:
                     st.image(Tata_img, caption='', width=250)
            
            
            st.write(
                """
                 
                """
            )
    #st.write("---") # addind a horizonatal line
    
# --- TECH STACK / SKILLS ---
if selected == "Data Stack":
    with st.container():
        st.write(
                """
                🔗 **Building the Data Bridge: From Raw Information to Business Gold** 🚀

- 📈 **Apache Spark**: My journey starts with Spark, where I ignite raw data into blazing insights. Whether it's massive data sets or real-time streaming, Spark's my trusted companion.
- 🐍 **Python**: As I delve deeper, Python becomes my secret potion. I craft data-driven spells with Pandas, NumPy, and Sci-kit Learn, unlocking hidden patterns and trends.
- 🧠 **Machine Learning**: My next adventure leads me to the world of machine learning. With scikit-learn, XGBoost, and TensorFlow, I build predictive models that anticipate the future.
- 🌐 **AWS**: The cloud beckons, and AWS is my playground. I orchestrate data pipelines using AWS Lambda, dance with data lakes on S3, and let EC2 instances run my experiments.
- 📊 **Tableau**: To visualize is to enlighten. With Tableau, I sculpt data into beautiful stories, empowering stakeholders to make informed decisions effortlessly.
- 🔧 **Serverless Computing**: Serverless is my latest enchantment. I conjure up serverless functions in AWS, Azure, and Google Cloud, weaving cost-effective spells into my data architecture.
            """)
        
        col1, col2 = st.columns((2,1))
        with col1:
            #st.subheader("Tech Stack / Skillsets")
            st.write(
                """
                
| Domain    | Tools                         |
|-------------|----------------------------|
| Languages | Python, C++, Java, HTML, CSS |
| Libraries | Pandas, Numpy, MatplotLib, Seaborn, Geopandas, Scikit-learn|
| Databases | MySQL, MongoDB |
| Cloud Platfoms | AWS EC2, S3 etc |
| Misc  | Spark, Docker, Airflow, Kafka, Git/github |
                
                """
            )

        with col2:
            st.image(computing_img, caption='', width=250)
            

       

# adding some styles from local machine via function defined above
local_css("css/styles.css") #  To get rid of the Streamlit branding stuff @ lower left page

