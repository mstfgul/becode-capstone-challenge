import os
import sys
from scrapping_final import main

if __name__ == "__main__":
    #main()
    print(f"Using Python executable: {sys.executable}")
    os.system(f"{sys.executable} -m streamlit run streamlit_file.py")