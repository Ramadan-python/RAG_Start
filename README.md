# Mini rag 
this is minimal implementation for RAG Answer Question project

# Requirments 
python 3.8 ot later 

#### install python using miniconda 

1) install miniconda from [here]"https://anaconda.com/api/installers/Miniconda3-latest-Windows-x86_64.exe"

2)creating new enviroment using the below command 
""" Bash
* conda create -n "Name of enviromengt"

""" bash
3) activate the enviroment by this commend 

* conda activate "name of enviroment"

## installtion
""" install packages """"
""" bash
pip install -r requiements.txt
"""
## install eviroment variable 
''' bash
cp .env.example .env
'''
# set your enviroments vaiable inside .env Like "OPENAI_API_KEY=""
OPENAI_API_KEY=''

# Run FastAPI server

'''bash
uvicorn main:app --reload --host 0.0.0.0 --port 5000
'''


