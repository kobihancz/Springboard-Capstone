import os
os.system('cd .kaggle')
os.system('kaggle datasets download -d worldbank/world-development-indicators')
os.system('mv ~/world-development-indicators.zip /Users/kobihancz/Desktop/Springboard_Capstone')
os.system('unzip world-development-indicators.zip')