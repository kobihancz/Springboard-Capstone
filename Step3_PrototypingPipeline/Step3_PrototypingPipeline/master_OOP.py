from data_collection import DataSets
from data_cleaning import WorldIndicators
import pandas as pd
import zipfile

DATASET = 'worldbank/world-development-indicators'

COUNTRIES = pd.read_csv('/Users/kobihancz/Desktop/Springboard_Capstone/Dataset/Country.csv')
INDICATORS  = pd.read_csv('/Users/kobihancz/Desktop/Springboard_Capstone/Dataset/Indicators.csv')
SERIES = pd.read_csv('/Users/kobihancz/Desktop/Springboard_Capstone/Dataset/Series.csv')
COUNTRY_NOTES = pd.read_csv('/Users/kobihancz/Desktop/Springboard_Capstone/Dataset/CountryNotes.csv')
SERIES_NOTES = pd.read_csv('/Users/kobihancz/Desktop/Springboard_Capstone/Dataset/SeriesNotes.csv')
FOOT_NOTES = pd.read_csv('/Users/kobihancz/Desktop/Springboard_Capstone/Dataset/Footnotes.csv')


DataSet = DataSets()
DataSet.dataset_dwnload(DATASET)

word_indicators = WorldIndicators()
word_indicators.transform_countries()
word_indicators.transform_indicators()


