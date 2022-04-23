Current Sate of the Capstone Project: Final Submission 

Data Exploration: After locally ingesting the data its time to explore it. In this step step I Used pandas/Numbpy to explore the different datframes in a Jupyter Notbook. I had to make a lot of decisions on what kinds of functions I would use in oder to find value in the different types of data. I had to decide what aspects of the data where clear/clean snd what aspects needed to be explored even more. 

Data cleaning: In this step I then went onto cleaning the data based on the information I unvieled during the exploration phase. I used Pandas to turn the csv data into datframes which then allowed me to manipulate these datframes to enforce the changes I wanted to make. 

Prototyping the Pipeline: In this Step I put all of the previouse stems together, This included ingestion, cleaning, and importing to the database. I had to make a decision on what the best kind of storage would be in order to correctly store the datt so it would be easily accessed and could scale up as data size grew. 

Scaling the Prototype: In this step I had to use Apchche spark to scale upp the processing power of my code. I had to make decisions on what parts of my previouse code needed to be changed to allow the piping to be done through apache spark. I eventually decided that for now the best aspect to scale up would be the cleaning portion so thats what I did. I opened a spark session and cleaned the data in there before importing it to the database. 

Diagram: 

Next Steps: I will continue to work on this capstone project to allow for more relevant features such as cloud storage, EOD Batch Loads, analytical ETL, and a dashboard to easily view the pipeline.



