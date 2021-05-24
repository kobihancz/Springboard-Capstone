import pandas as pd
import mysql.connector
import csv

class DatabaseHandler:
    def __init__(self,user,password,database,host = '127.0.0.1',port = '3306'):
        self.user = user
        self.password = password
        self.database = database
        self.host = host
        self.port = port
        try:
            self.connection = mysql.connector.connect(user = user, 
                                        password = password,
                                        host = host,
                                        port = port,
                                        database = database)
        except Exception as ex:
            print(f"Error while connecting to {database} as {user}", ex)
        print(f"Sucssesfully connected to {database} as {user}")

    # def load_country_data(self,file_path_csv):
    #     insert_stmt = ("INSERT INTO country " 
    #                 "(CountryCode, ShortName, LongName, Alpha2Code, CurrencyUnit, SpecialNotes, Region, IncomeGroup, Wb2Code, "
    #                 "NationalAccountsBaseYear, NationalAccountsReferenceYear, SnaPriceValuation, LendingCategory, OtherGroups, SystemOfNationalAccounts,"
    #                 "PppSurveyYear, BalanceOfPaymentsManualInUse, ExternalDebtReportingStatus, SystemOfTrade, GovernmentAccountingConcept,"
    #                 "ImfDataDisseminationStandard, LatestPopulationCensus, LatestHouseholdSurvey,SourceOfMostRecentIncomeAndExpenditureData, " 
    #                 "VitalRegistrationComplete, LatestAgriculturalCensus, LatestIndustrialData, LatestTradeData, LatestWaterWithdrawalData) " 
    #                 "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
    #     with self.connection.cursor() as cursor:
    #         with open(file_path_csv) as csv_file:
    #             try:
    #                 for row in csv.reader(csv_file):
    #                     cursor.execute(insert_stmt,row)
    #                 print("Successfully added country CSV into Capstone_DB")

    #             except Exception as ex:
    #                 print("Error while reading country CSV into Capstone_DB", ex)
       
        
    #     self.connection.commit()

    # def load_country_notes_data(self,file_path_csv):
    #     insert_stmt = ("INSERT INTO country_notes" 
    #                 "('Countrycode', 'Seriescode', 'Description')" 
    #                 "VALUES(%s,%s,%s)")
    #     with self.connection.cursor() as cursor:
    #         with open(file_path_csv) as csv_file:
    #             try:
    #                 for row in csv.reader(csv_file):
    #                     cursor.execute(insert_stmt,row)
    #                 print("Successfully added country_notes CSV into Capstone_DB")
                
    #             except Exception as ex:
                    # print("Error while reading country_notes CSV into Capstone_DB", ex)
        
    #     self.connection.commit()

    def load_footnotes_data(self,file_path_csv):
        insert_stmt = ("INSERT INTO footnotes " 
                    "(Countrycode, Seriescode, Year, Description) " 
                    "VALUES (%s,%s,%s,%s)")
        with self.connection.cursor() as cursor:
            with open(file_path_csv) as csv_file:
                try:
                    for row in csv.reader(csv_file):
                        cursor.execute(insert_stmt,row)
                    print("Successfully added footnotes CSV into Capstone_DB")

                except Exception as ex:
                    print("Error while reading footnotes CSV into Capstone_DB", ex)
        
        self.connection.commit()

    # def load_indicators_data(self,file_path_csv):
    #     insert_stmt = ("INSERT INTO indicators" 
    #                 "('CountryName', 'CountryCode', 'IndicatorName', 'IndicatorCode', 'Year', 'Value')" 
    #                 "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
    #     with self.connection.cursor() as cursor:
    #         with open(file_path_csv) as csv_file:
    #             try:
    #                 for row in csv.reader(csv_file):
    #                     cursor.execute(insert_stmt,row)
    #                 print("Successfully added indicaators CSV into Capstone_DB")

    #             except Exception as ex:
    #                 print("Error while reading indicators CSV into Capstone_DB", ex)
        
    #     self.connection.commit()

    # def load_series_data(self,file_path_csv):
    #     insert_stmt = ("INSERT INTO series" 
    #                 "('SeriesCode', 'Topic', 'IndicatorName', 'LongDefinition', 'Periodicity', 
    #                 'AggregationMethod', 'LimitationsAndExceptions', 'NotesFromOriginalSource', 
    #                 'GeneralComments', 'Source', 'StatisticalConceptAndMethodology', 'DevelopmentRelevance', 'LicenseType')" 
    #                 "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
    #     with self.connection.cursor() as cursor:
    #         with open(file_path_csv) as csv_file:
    #             try:
    #                 for row in csv.reader(csv_file):
    #                     cursor.execute(insert_stmt,row)
    #                 print("Successfully added series CSV into Capstone_DB")

    #             except Exception as ex:
    #                 print("Error while reading series CSV into Capstone_DB", ex)
        
    #     self.connection.commit()

    # def load_series_notes(self,file_path_csv):
    #     insert_stmt = ("INSERT INTO sales" 
    #                 "('Seriescode', 'Year', 'Description')" 
    #                 "VALUES(%s,%s,%s)")
    #     with self.connection.cursor() as cursor:
    #         with open(file_path_csv) as csv_file:
    #             try:
    #                 for row in csv.reader(csv_file):
    #                     cursor.execute(insert_stmt,row)
    #                 print("Successfully added series_notes CSV into Capstone_DB")

    #             except Exception as ex:
    #                 print("Error while reading series_notes CSV into Capstone_DB", ex)
        
    #     self.connection.commit()

pipeline = DatabaseHandler('root', 'Riley123$','Capstone_DB')
# pipeline.load_country_data('/Users/kobihancz/Desktop/Springboard_Capstone/Dataset/Country.csv')
# pipeline.load_country_notes_data('/Users/kobihancz/Desktop/Springboard_Capstone/Dataset/CountryNotes.csv')
pipeline.load_footnotes_data('/Users/kobihancz/Desktop/Springboard_Capstone/Dataset/Footnotes.csv')
# pipeline.load_indicators_data('/Users/kobihancz/Desktop/Springboard_Capstone/Dataset/Indicators.csv')
# pipeline.load_series_data('/Users/kobihancz/Desktop/Springboard_Capstone/Dataset/Series.csv')
# pipeline.load_series_notes('/Users/kobihancz/Desktop/Springboard_Capstone/Dataset/SeriesNotes.csv')

changes test ghghkdkd


# insert_stmt = ("INSERT INTO country " 
#                     "('CountryCode', 'ShortName', 'LongName', 'Alpha2Code', 'CurrencyUnit', 'SpecialNotes', 'Region', 'IncomeGroup', 'Wb2Code', "
#                     "'NationalAccountsBaseYear', 'NationalAccountsReferenceYear', 'SnaPriceValuation', 'LendingCategory', 'OtherGroups', 'SystemOfNationalAccounts',"
#                     "'PppSurveyYear', 'BalanceOfPaymentsManualInUse', 'ExternalDebtReportingStatus', 'SystemOfTrade', 'GovernmentAccountingConcept',"
#                     "'ImfDataDisseminationStandard', 'LatestPopulationCensus', 'LatestHouseholdSurvey','SourceOfMostRecentIncomeAndExpenditureData', " 
#                     "'VitalRegistrationComplete', 'LatestAgriculturalCensus', 'LatestIndustrialData', 'LatestTradeData', 'LatestWaterWithdrawalData') " 
#                     "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")

