import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi

DATASET = 'worldbank/world-development-indicators'

class DataSetDownloader:

    def dataset_dwnload(self,datset):
        api = KaggleApi()
        api.authenticate()

        api.dataset_download_files(datset)

        with zipfile.ZipFile('/Users/kobihancz/Desktop/Springboard-Capstone/world-development-indicators.zip', 'r') as zipref:
            zipref.extractall('/Users/kobihancz/Desktop/Springboard-Capstone/Dataset')

DataSet = DataSetDownloader()
DataSet.dataset_dwnload(DATASET)
