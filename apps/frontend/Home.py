import streamlit as st

st.set_page_config(page_title="GPT Smart Search", page_icon="📖", layout="wide")

st.image("https://user-images.githubusercontent.com/113465005/226238596-cc76039e-67c2-46b6-b0bb-35d037ae66e1.png")

st.header("MSUS OpenAI Accelerator VBD - Web Frontend")


st.markdown("---")
st.markdown("""
    This engine finds information from the following:
    - ~10k [Computer Science Publications in Arxiv from 2020-2021](https://www.kaggle.com/datasets/1b6883fb66c5e7f67c697c2547022cc04c9ee98c3742f9a4d6c671b4f4eda591)
    - ~90k [COVID-19 research articles from the CORD19 dataset](https://github.com/allenai/cord19)
    - [Covid Tracking Project Dataset](https://covidtracking.com/). Azure SQL with information of Covid cases and hospitalizations in the US from 2020-2021.
    - The Bot Interface is just a window to a Bot Service app hosted in Azure. 
    
    **👈 Select a demo from the sidebar** to see an example of a Search Interface, and a Bot Interface.

"""
)
st.markdown("---")
