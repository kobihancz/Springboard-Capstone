import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi

DATASET = 'world-development-indicators'
OWNER = 'worldbank'

def dataset_dwnload(datset,owner):
    api = KaggleApi()
    api.authenticate()
    api.datasets_download(datset, owner)

    with zipfile.ZipFile() as zipref:
        zipref.extractall()

dataset_dwnload(DATASET,OWNER)






