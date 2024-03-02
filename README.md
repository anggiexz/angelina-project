#Setup environment

conda create --name main-ds python=3.11.8
conda activate main-ds
pip install numpy pandas matplotlib jupyter streamlit 

#Run steamlit app

streamlit run Hello.py
