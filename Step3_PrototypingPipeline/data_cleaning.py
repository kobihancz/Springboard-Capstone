import pandas as pd

COUNTRIES = pd.read_csv('/Users/kobihancz/Desktop/Springboard_Capstone/Dataset/Country.csv')
INDICATORS  = pd.read_csv('/Users/kobihancz/Desktop/Springboard_Capstone/Dataset/Indicators.csv')
SERIES = pd.read_csv('/Users/kobihancz/Desktop/Springboard_Capstone/Dataset/Series.csv')
COUNTRY_NOTES = pd.read_csv('/Users/kobihancz/Desktop/Springboard_Capstone/Dataset/CountryNotes.csv')
SERIES_NOTES = pd.read_csv('/Users/kobihancz/Desktop/Springboard_Capstone/Dataset/SeriesNotes.csv')
FOOT_NOTES = pd.read_csv('/Users/kobihancz/Desktop/Springboard_Capstone/Dataset/Footnotes.csv')

class WorldIndicators:

    # remove all country rows that are more categorical and have currency units of NaN 
    def transform_countries(self):
        cleaned_countries_table = COUNTRIES[COUNTRIES['CurrencyUnit'].notna()]
        # drops these colmuns because they are either redundant or do not provide enough entries to be relevant
        cleaned_countries_table.drop(['ShortName','NationalAccountsReferenceYear','AlternativeConversionFactor'], inplace = True, axis =1)
        self.write_to_csv(cleaned_countries_table, 'cleanedCountrys.csv')

    #create a table with the top 10 or 20 indicators that are important to the problem statement, for each country 
    def transform_indicators(self):
        important_indicators = ['Population, total', 'Population growth (annual %)', "Rural population (% of total population)", 
                                'Urban population (% of total)', 'Rural population', 'Urban population', 'Urban population growth (annual %)',
                                'Rural population growth (annual %)', 'Death rate, crude (per 1,000 people)', 'Birth rate, crude (per 1,000 people)', 
                                'Population, ages 0-14 (% of total)', 'Population, ages 15-64 (% of total)', 'Population ages 65 and above (% of total)',
                                'Life expectancy at birth, female (years)', 'Life expectancy at birth, male (years)', 'Life expectancy at birth, total (years)',
                                'Mortality rate, adult, female (per 1,000 female adults)', 'Mortality rate, adult, male (per 1,000 male adults)', 
                                'Merchandise exports (current US$)', 'Merchandise imports (current US$)', 'Merchandise exports by the reporting economy (current US$)',
                                'Merchandise exports by the reporting economy, residual (% of total merchandise exports)', 'Merchandise imports by the reporting economy (current US$)', 
                                'Merchandise imports by the reporting economy, residual (% of total merchandise imports)', 'Merchandise imports from high-income economies (% of total merchandise imports)', 
                                'Merchandise exports to high-income economies (% of total merchandise exports)', 'Merchandise imports from developing economies in South Asia (% of total merchandise imports)', 
                                'GDP at market prices (current US$)', 'GDP per capita (current US$)', 'GDP growth (annual %)', 'GDP per capita growth (annual %)',
                                'Imports of goods and services (% of GDP)', 'Exports of goods and services (% of GDP)', 'Imports of goods and services (current US$)', 'xports of goods and services (current US$)', 
                                'Merchandise exports to economies in the Arab World (% of total merchandise exports)', 'Merchandise imports from economies in the Arab World (% of total merchandise imports)',
                                'Merchandise imports from developing economies in Sub-Saharan Africa (% of total merchandise imports)', 'Merchandise exports to developing economies in Sub-Saharan Africa (% of total merchandise exports)',
                                'Merchandise exports to developing economies in Latin America & the Caribbean (% of total merchandise exports)', 'Merchandise imports from developing economies in Latin America & the Caribbean (% of total merchandise imports)', 
                                'Manufactures imports (% of merchandise imports)', 'Food imports (% of merchandise imports)', 'Fuel imports (% of merchandise imports)', 'Ores and metals imports (% of merchandise imports)', 
                                'Agricultural raw materials imports (% of merchandise imports)', 'Merchandise imports from developing economies outside region (% of total merchandise imports)', 'Merchandise exports to developing economies outside region (% of total merchandise exports)', 
                                'Arms imports (SIPRI trend indicator values)', 'Merchandise imports from developing economies in East Asia & Pacific (% of total merchandise imports)', 'Exports of goods and services (annual % growth)', 
                                'Imports of goods and services (annual % growth)']

        important_indicators_table = INDICATORS[INDICATORS['IndicatorName'].isin(important_indicators)]
        self.write_to_csv(important_indicators_table, 'importantIndicators.csv')

    def write_to_csv(self,dataframeObj,filename = str):
        dataframeObj.to_csv('/Users/kobihancz/Desktop/Springboard_Capstone/Dataset/'+filename)



