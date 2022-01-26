from fastapi import FastAPI
from pydantic import BaseModel
import socket
from web_scraping import *
from download_file import download_file
app = FastAPI()

class locationInfo(BaseModel):
    zip_code_list: list



@app.get("/")
async def root():
    return {"hostname": socket.gethostname(),"app_version":"version-2.0.2"}

@app.get("/download_file")
async def download_sample():
    return {"result": download_file(),"status":"file download"}
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

@app.post("/get_locations_for_zip/")
def location_module(value_list: locationInfo):
    results_list = []
    for zips in value_list.zip_code_list:
        try:
            results_list.append(get_results(zips))
        except:
            pass
    return {"status": "Success", "results": results_list}