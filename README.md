# Web-Scraping-and-Sentiment-Analysis 🤗😐😔

## Introduction 🤔
This project leverages Scrapy to fetch reviews of products on Amazon based on queries. The extracted information includes user reviews, usernames, review titles, ratings, product id, product types, dates, and locations. The scraping process can be performed for a specified number of pages or product codes. Sentiment analysis was performed using RoBERTa and VADER models with data obtained from more than 3000 products. This project contains a summary of the problems that may happen to you while fetching data from the web...

## Workflow 🛠️

### 1. Product Codes (asin) Retrieval with BeautifulSoup:
Product codes are obtained using the ```BeautifulSoup``` and ```Request``` libraries. Go to ```asin_list.py```.
### 2. Scrapy Scraping Operations:
Scrapy is employed to perform scraping operations on Amazon pages.

• Create a Python Virtual Environment (I recommend you to use PyCharm).

• In terminal ```pip install scrapy```, ```scrapy startproject```

• Once you are done with adjusting all your codes, you can run it in terminal ```scrapy crawl your_bot_name```

### 3. Bypassing Amazon with ScrapeOps Proxy:
ScrapeOps Proxy is utilized to bypass Amazon restrictions during scraping. This Amazon spider uses ScrapeOps Proxy as the proxy solution. ScrapeOps has a free plan that allows you to make up to 1,000 requests per month which makes it ideal for the development phase, but can be easily scaled up to millions of pages per month if needs be.

[ScrapeOps Proxy](https://scrapeops.io/) 

• ```pip install scrapeops-scrapy-proxy-sdk```.

• Do not forget to add  your API key to the ```SCRAPEOPS_API_KEY``` in the ```settings.py``` file.
### 4. Data Storage in MySQL:
Extracted data is stored in a MySQL database. ```DO NOT FORGET YOUR DATABASE PASSWORD!```
### 5. Transfer to Jupyter Notebook:
Data from the database is transferred to a Jupyter Notebook. Check the ```clean-amazons-reviews-en.ipynb``` in notebooks folder.
### 6. Data Manipulation and Exploratory Data Analysis with Python Libraries:
Python, Pandas, Seaborn, Matplotlib, and other libraries are used for data manipulation and EDA. Duplicate values, dtypes, separating columns... Eventually, non-English comments are removed.
### 7. Sentiment Analysis using Vader and Roberta Models:
Sentiment analysis is performed using the ```VADER``` and ```RoBERTa``` models. Check ```sentiment-analysis.ipynb```
### 8. Handling Token Limitations:
A solution is developed to address issues arising from analyzing texts with more than 512 tokens.
### 9. DataFrame Comparison:
The obtained values are added to a data frame and compared.
### 10. Data Visualization with Graphs:
Graphs are generated to visualize the results.
### 11. ```.csv``` Files:
You can find all the data in ```datas``` folder. 

•```raw_data.csv``` represents the data from scraping.

•```english_reviews.csv```  represents the data after data manipulation.

•```roberta_and_vader_df``` represents the data that includes sentiment analysis by RoBERTa and VADER.

# Conclusion 👇🏼
In conclusion, this project provides a comprehensive pipeline for scraping Amazon reviews, storing the data in a MySQL database, performing data analysis and sentiment analysis, and visualizing the results through graphs. The use of ScrapeOps Proxy enhances the scraping process, ensuring efficient data extraction from Amazon. The developed solution for handling token limitations demonstrates the project's adaptability and problem-solving approach.

# Notes 📢
You can find ```.ipynb``` files in the ```notebooks``` folder. Detailed explanations of the codes and my comments are available in the notebook.


If you have any suggestions, questions, or ideas, I am all ears! Your input is invaluable, and I would appreciate it if you could help improve my codes. Feel free to reach out with your feedback; it would be greatly welcomed!🧐
