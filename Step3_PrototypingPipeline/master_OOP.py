from data_collection import DataSetDownloader
from data_cleaning import DatasetCleaner
from import_to_db import DatabaseHandler
import pandas as pd
import zipfile

DATASET = 'worldbank/world-development-indicators'

COUNTRIES = pd.read_csv('/Users/kobihancz/Desktop/Springboard-Capstone/Dataset/Country.csv')
INDICATORS  = pd.read_csv('/Users/kobihancz/Desktop/Springboard-Capstone/Dataset/Indicators.csv')
SERIES = pd.read_csv('/Users/kobihancz/Desktop/Springboard-Capstone/Dataset/Series.csv')
COUNTRY_NOTES = pd.read_csv('/Users/kobihancz/Desktop/Springboard-Capstone/Dataset/CountryNotes.csv')
SERIES_NOTES = pd.read_csv('/Users/kobihancz/Desktop/Springboard-Capstone/Dataset/SeriesNotes.csv')
FOOT_NOTES = pd.read_csv('/Users/kobihancz/Desktop/Springboard-Capstone/Dataset/Footnotes.csv')

#Downloads DataSet
DataSet = DataSetDownloader()
DataSet.dataset_dwnload(DATASET)
print("Downloaded Dataset")

#cleans DataSet
Clean = DatasetCleaner()
Clean.clean_foot_notes()
Clean.clean_series_notes()
Clean.clean_series()
Clean.clean_countries()
Clean.clean_indicators
print("Cleaned Dataset")

# #Adds Cleaned Data to the Database
pipeline = DatabaseHandler('root', 'Riley123$','Capstone_DB')
pipeline.load_country_data('/Users/kobihancz/Desktop/Springboard-Capstone/Dataset/Country.csv')
pipeline.load_country_notes_data('/Users/kobihancz/Desktop/Springboard-Capstone/Dataset/CountryNotes.csv')
pipeline.load_footnotes_data('/Users/kobihancz/Desktop/Springboard-Capstone/Dataset/Footnotes.csv')
pipeline.load_indicators_data('/Users/kobihancz/Desktop/Springboard-Capstone/Dataset/Indicators.csv')
pipeline.load_series_data('/Users/kobihancz/Desktop/Springboard-Capstone/Dataset/Series.csv')
pipeline.load_series_notes('/Users/kobihancz/Desktop/Springboard-Capstone/Dataset/SeriesNotes.csv')
print("Uploaded Dataset to Database")




