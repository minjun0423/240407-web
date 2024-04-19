#from typing import Union

from fastapi import FastAPI
#from pydantic import BaseModel

import requests

app = FastAPI()

    
@app.get("/")
def read_root():
    URL = "https://bigdata.kepco.co.kr/openapi/v1/powerUsage/industryType.do?year=2020&month=11&metroCd=11&cityCd=12&apiKey=69viVTSCMlJ552B9O243czcn718eth0C5691acbA&returnType=json"

    contents = requsts.get(URL).text

    return {"message": contents}

@app.get("/home")
def home():
    return {"message": "home!"}