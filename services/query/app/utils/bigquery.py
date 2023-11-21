import pandas_gbq
from google.oauth2 import service_account

"""
This module handles the creation and retrieving of the requests   
made to the BigQuery dataset to be used in the different endpoints.
"""

"""
Here we get the credentials of the bigquery project through a service account.
For more information about service accounts: https://cloud.google.com/iam/docs/service-account-overview
"""
credentials = service_account.Credentials.from_service_account_file('./bigquery-service-account.json')

# Get data specifying country_code, indicator, and optionally a year.
def get_data(country_code: str, indicator: str, year: str | None) -> any: 
    """
    Conditionally check if the user specified a year for the query, if not
    disregard the 'AND YEAR > {user_input'} clause, otherwise, add it to
    the SQL StatementRole
    """
    if year == None:
        query = f"""
        SELECT
            value,
            year,
            country_name,
            country_code,
            indicator_name,
            indicator_code,
            AVG(value) AS average
        FROM
            `bigquery-public-data.world_bank_intl_education.international_education`
        WHERE 
            country_code = '{country_code}'
            AND indicator_code = '{indicator}'  
        GROUP BY
            country_name, country_code, indicator_name, indicator_code, value, year
        ORDER BY
            average ASC
        """
    else:
        query = f"""
        SELECT
            value,
            year,
            country_name,
            country_code,
            indicator_name,
            indicator_code,
            AVG(value) AS average
        FROM
            `bigquery-public-data.world_bank_intl_education.international_education`
        WHERE 
            country_code = '{country_code}'
            AND indicator_code = '{indicator}'  
            AND year >= {year}
        GROUP BY
            country_name, country_code, indicator_name, indicator_code, value, year
        ORDER BY
            average ASC
        """

    # Loads the data of the query, returns a pandas DataFrame
    df = pandas_gbq.read_gbq(query, credentials=credentials) 

    # Transform the data to be utilized in the frontend
    result_list = [
        {
            'value': value,
            'year': year,
            'countryName': country_name,
            'countryCode': country_code,
            'indicatorName': indicator_name,
            'indicatorCode': indicator_code
        } for value, year, country_name, country_code, indicator_name, indicator_code in zip(df['value'].astype(int), df['year'].astype(int), df['country_name'], df['country_code'], df['indicator_name'], df['indicator_code'])
    ] 

    return result_list

# Get data specifying 1 or more country codes
def get_multiple(country_codes: list[str], indicator: str, year: str) -> any:
    
    query = f"""
    SELECT
        value,
        year,
        country_name,
        country_code,
        indicator_name,
        indicator_code,
        AVG(value) AS average
    FROM
        `bigquery-public-data.world_bank_intl_education.international_education`
    WHERE   
        country_code IN {tuple(country_codes)}
        AND indicator_code = '{indicator}' 
        AND year > {int(year)}
    GROUP BY
        country_name, country_code, indicator_name, indicator_code, value, year
    ORDER BY
        average ASC
    """ 

    df = pandas_gbq.read_gbq(query, credentials=credentials) 

    # Transform the data to be utilized in the frontend
    result_list = [
        {
            'value': value,
            'year': year,
            'country_name': country_name,
            'country_code': country_code,
            'indicator_name': indicator_name,
            'indicator_code': indicator_code
        } for value, year, country_name, country_code, indicator_name, indicator_code in zip(df['value'].astype(int), df['year'].astype(int), df['country_name'], df['country_code'], df['indicator_name'], df['indicator_code'])
    ] 

    return result_list

"""
Get all indicators from BigQuery for the user in the frontend to select
"""
def get_all_indicators() -> any:

    query = f"""
    SELECT DISTINCT
        indicator_name, indicator_code 
    FROM
        `bigquery-public-data.world_bank_intl_education.international_education`
    LIMIT 50
    """

    df = pandas_gbq.read_gbq(query, credentials=credentials)   

    result_list = [{'value': key, 'label': value} for key, value in zip(df['indicator_code'], df['indicator_name'])]
 
    return result_list

"""
Get all countries from BigQuery for the user in the frontend to select
"""
def get_all_countries() -> any:

    query = f"""
    SELECT DISTINCT
        country_name, country_code 
    FROM
        `bigquery-public-data.world_bank_intl_education.international_education`
    """

    df = pandas_gbq.read_gbq(query, credentials=credentials) 

    result_list = [{'value': key, 'label': value} for key, value in zip(df['country_code'], df['country_name'])]
     
    return result_list

