"""
Extract a dataset from a URL like Kaggle or data.gov. JSON or CSV formats tend to work well

food dataset
"""
import requests

def extract(url="https://raw.githubusercontent.com/nogibjj/yijia_ids706_miniProj3/refs/heads/main/rdu-weather-history.csv", 
            file_path="data/rdu-weather-history.csv"):
    """"Extract a url to a file path"""
    with requests.get(url) as r:
        with open(file_path, 'wb') as f:
            f.write(r.content)
    return file_path



