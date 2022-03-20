import pandas as pd
from serpapi import GoogleSearch
import sqlite3
import datetime as dt

import config

def google_job_search(job_title, city_state, post_age="week"):
    '''
    job_title(str): "Data Scientist", "Data Analyst"
    city_state(str): "Denver, CO"
    post_age,(str)(optional): "3day", "week", "month"
    '''
    params = {
            "engine": "google_jobs",
            "q": f"{job_title} {city_state}",
            "hl": "en",
            "api_key": config.SerpAPIkey,
            "chips":f"date_posted:{post_age}", 
            }
    search = GoogleSearch(params)
    results = search.get_dict()
    jobs_results = results['jobs_results']
    job_columns = ['title', 'company_name', 'location', 'description']
    df = pd.DataFrame(jobs_results, columns=job_columns)
    return df

def sql_dump(df, db, table):
    con = sqlite3.connect(db) #db="data\jobs.db"
    df.to_sql(table, con, if_exists='append') #table='jobs_data'
    con.close()

def main(job_list, city_state_list):
    job_columns = ['title', 'company_name', 'location', 'description']
    main_df = pd.DataFrame(columns=job_columns)
    for job in job_list:
        for city_state in city_state_list:
            df_10jobs = google_job_search(job, city_state, post_age="month")
            main_df = main_df.append(df_10jobs)
    date = dt.datetime.today().strftime('%Y-%m-%d')
    main_df['retrieve_date'] = date
    sql_dump(main_df, 'data/jobs', 'google_jobs')
    return main_df

if __name__ == "__main__":
    job_list = ["Data Scientist", "Data Analyst", "Data Engineer", 
                "Machine Learning Engineer", "Business Intelligence Analyst"]
    city_state_list = ["Atlanta, GA", "Austin, TX", "Boston, MA", "Chicago, IL", 
                    "Denver, CO", "Dallas-Ft. Worth, TX", "Los Angeles, CA",
                    "New York City, NY", "San Francisco, CA", "Seattle, WA"]
    main(job_list, city_state_list)