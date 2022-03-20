## Analyzing Trending "Data" Jobs

As a Data Scientist, I was interested in finding out what languages, cloud platforms, and tools were in demand by some of our more common data-related jobs. One way to get these insights is to look at what employers are mentioning in their job postings. There are several great job board websites out there like Google Jobs, LinkedIn, and Indeed. Since I’m an active user in the first two platforms I decided to scrape the third.

### Data Collection

The "BS4_Indeed_functional.py" file is my primary way of scraping for job meta data. A more detailed description of how I created it can be found in this medium article [enter url here.] The job meta data is saved in a SQLite database which is stored in the data folder, everyonce and a while I save all the results down as a .csv since a lot of people are more familiar with that format. 

Another way to get job meta data without scraping is using the google jobs SerpAPI which the file "SerpAPI_GoogleJobs.py" utilizes. They have a free trail that allows 100 calls, you can continue to use it for free afterwards but be aware that there is a limit of 10 calls per hour for the free tier after the initial trail. 

### Data Analysis

The "Clean_Analyze_Jobs.ipynb" notebook is my primary way of analyzing the job meta data, mainly the job descriptions. A more detailed description of my analysis can be found in this medium article [enter url here]. 