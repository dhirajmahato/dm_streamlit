import base64
import streamlit as st
from PIL import Image

# page_config is what is seen in broswer tab
st.set_page_config(
    page_title="Contact",
    page_icon="envelope",
    layout="wide",
    initial_sidebar_state="expanded"   # use'auto' for first visit
)



# Define custom CSS to set the SVG as background
custom_css1 = f"""
<style>
  .stApp {{
        background-image: url('https://cdn.svgator.com/images/2023/06/email-character-preloader.gif');
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: right;
    }}
</style>
"""

# Display the custom CSS with the SVG background
st.markdown(custom_css1, unsafe_allow_html=True) 
#--------------------------------------------------------------
def local_css(file_name):    #import local machine css file
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

#----------------def used functions -------------------------------

def social_icons(width=24, height=24, **kwargs):
    icon_template = '''
    <a href="{url}" target="_blank" style="margin-right: 20px;">
    <img src="{icon_src}" alt="{alt_text}" width="{width}" height="{height}">
    </a>
    '''

    icons_html = ""
    for name, url in kwargs.items():
        icon_src = {
            "youtube": "https://img.icons8.com/ios-filled/100/ff8c00/youtube-play.png",
            "linkedin": "https://img.icons8.com/ios-filled/100/0072b1/linkedin.png",
            "github": "https://img.icons8.com/ios-filled/100/github--v2.png",
            "email": "https://img.icons8.com/color/48/gmail-new.png"
        }.get(name.lower())

        if icon_src:
            icons_html += icon_template.format(url=url, icon_src=icon_src, alt_text=name.capitalize(), width=width, height=height)

    return icons_html       



#----- After navigation bar------------
with st.container():
    text_column, mid, image_column = st.columns((1,0.2,0.5))
    with text_column:
        st.write("Let's connect! You may either reach out to me at dhiraj.mahato.iitbhu@gmail.com")
        st.write("Alternatively, feel free to check out my social accounts below!")
        linkedin_url = "https://www.linkedin.com/in/dhirajkrmahato/"
        github_url = "https://github.com/dhirajmahato"
        email_url = "mailto:dhiraj.mahato.iitbhu@gmail.com"
        st.markdown(
            social_icons(32, 32, LinkedIn=linkedin_url, GitHub=github_url, Email=email_url),
            unsafe_allow_html=True)
        st.markdown("")

    with mid:
        st.empty()
    with image_column:
        st.empty()
        #st.image(img_ifg)




# adding some styles from local machine via function defined above
local_css("css/styles.css") #  To get rid of the Streamlit branding stuff @ lower left page
