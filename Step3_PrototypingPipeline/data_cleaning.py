import pandas as pd

COUNTRIES = pd.read_csv('/Users/kobihancz/Desktop/Springboard-Capstone/Dataset/Country.csv')
INDICATORS  = pd.read_csv('/Users/kobihancz/Desktop/Springboard-Capstone/Dataset/Indicators.csv')
SERIES = pd.read_csv('/Users/kobihancz/Desktop/Springboard-Capstone/Dataset/Series.csv')
COUNTRY_NOTES = pd.read_csv('/Users/kobihancz/Desktop/Springboard-Capstone/Dataset/CountryNotes.csv')
SERIES_NOTES = pd.read_csv('/Users/kobihancz/Desktop/Springboard-Capstone/Dataset/SeriesNotes.csv')
FOOT_NOTES = pd.read_csv('/Users/kobihancz/Desktop/Springboard-Capstone/Dataset/Footnotes.csv')

class DatasetCleaner:
    def __init__(self):
        pass

    def write_to_csv(self,dataframeObj,filename = str):
        dataframeObj.to_csv('/Users/kobihancz/Desktop/Springboard-Capstone/Dataset/'+filename, index = False)

    # remove all columns that are close to 100% empty 
    def clean_countries(self):
        CLEANED_COUNTRIES = COUNTRIES.drop(['TableName','AlternativeConversionFactor','NationalAccountsReferenceYear'], axis =1)
        self.write_to_csv(CLEANED_COUNTRIES, 'Country.csv')
  
    def clean_indicators(self):
        INDICATORS['Value'] = INDICATORS['Value'].round(decimals=4)
        self.write_to_csv(INDICATORS, 'Indicators.csv')

    def clean_series(self):
        CLEANED_SERIES = SERIES.drop(['ShortDefinition', 'UnitOfMeasure', 'BasePeriod', 'OtherNotes', 'NotesFromOriginalSource', 'RelatedSourceLinks', 'OtherWebLinks', 'RelatedIndicators', 'StatisticalConceptAndMethodology'], axis =1)
        self.write_to_csv(CLEANED_SERIES, 'Series.csv')

# def clean_country_notes(self):
        
# Clean year column by turning the values into integers 
    def clean_series_notes(self):
        SERIES_NOTES['Year'] = SERIES_NOTES['Year'].str[2:]
        SERIES_NOTES['Year'] = SERIES_NOTES['Year'].astype(int) 
        self.write_to_csv(SERIES_NOTES, 'SeriesNotes.csv')

# Clean year column by turning the values into integers 
    def clean_foot_notes(self):
        FOOT_NOTES['Year'] = FOOT_NOTES['Year'].str[2:]
        FOOT_NOTES['Year'] = FOOT_NOTES['Year'].astype(int) 
        self.write_to_csv(FOOT_NOTES, 'Footnotes.csv')

TestClean = DatasetCleaner()
TestClean.clean_foot_notes()
TestClean.clean_series_notes()
TestClean.clean_series()
TestClean.clean_countries()
TestClean.clean_indicators()






