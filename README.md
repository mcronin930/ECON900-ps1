# ECON900-ps1
Problem Set 1
## Procedure
This repository contains 5 programs that should be run in the following order:
### 1) 1_boardgamegeek_request.py
This program scrapes board game data presented on the table located here: https://boardgamegeek.com/browse/boardgame/

The program loops through all the pages the table is located on and saves an html file for each page in the html_files folder.
The scraping process required the use of a webdriver to open each page in a browser. This was because the price data was populated
in the html code using java. Using urllib request would only return a html files that did not contain the prices.

### 2) 2_boardgamegeek_parse.py
This program parses relevant data from the pages saved in html_files and creates a dataframe saved in parsed_files. The challenge 
here was parsing the price data. Since some games have different prices reported, such as “List”, “New Amazon”, “Lowest Amazon”, 
“Amazon”, “iOs App”, no price, or any combination of the above, I chose to pull all the price text as a string and extract the price 
data in step 3.

### 3) 3_boardgamegeek_pricedata_clean.py

I wrote an additional data building program to clean my game data as well as extract the different prices for each game.
‘3_boardgamegeek_pricedata_clean.py’ cleans the data and splits the price string, described above, into individual observations 
for each price. The resulting dataframe has rows for each game and price type, where price type is “List”, “New Amazon”, 
“Lowest Amazon”, “Amazon”, or “iOs App”. If a game did not have a price listed, the price column would be missing for that game 
and price type. The resulting dataframe is saved in training_data.

### 4) Supervised Learning Programs
#### 4_boardgamegeek_linearmodel_price.py
Uses the linear model machine from sklearn to impute the missing price data.

#### 4_boardgamegeek_linearmodel_BGGrating.py
Uses the linear model machine from sklearn to create a machine that predicts geek ratings. K-fold cross validation is then used to score
the machine.

## Additional Files
The write up for this project is 'Supervised Learning To Impute Missing Data & Predict Ratings.pdf'
