

from NikeCA import QA, Snowflake

import configparser

config = configparser.ConfigParser()
config.read('config2.ini')

username = config['snowflake'].get('username')
warehouse = config['snowflake'].get('warehouse')
role = config['snowflake'].get('role')
database = config['snowflake'].get('database')

sf = Snowflake(username=username, warehouse=warehouse, role=role, database=database)

query = """
    SELECT 
        RETAILER_GEOGRAPHY_DISPLAY_NM
        , RETAILER_GEOGRAPHY_ID
        , CATEGORY
        , CHANNEL
        , DIVISION_DESC
        , STORE_ACCOUNT_TYPE_CD
        , EXPRESS_LANE
        , LICENSED_IND
        , RETAILER_SALES_PRICE_PRCNT_BUCKET
        , MIN(ACTIVITY_END_DT) AS MIN_TEST_DATE
        , MAX(ACTIVITY_END_DT) AS MAX_TEST_DATE
        , SUM(TOTAL_NET_SALES_AMT_TY) AS TEST_AMT
        , SUM(TOTAL_NET_SALES_UNITS_TY) AS TEST_UNITS
    FROM 
        NGP_DA_PROD.POS_T.POS_RTLR_SC_TREND_AGG_D0316
    WHERE
        ACTIVITY_END_DT BETWEEN '2023-01-07' AND '2023-03-04'
    GROUP BY 
        RETAILER_GEOGRAPHY_DISPLAY_NM
        , RETAILER_GEOGRAPHY_ID
        , CATEGORY
        , CHANNEL
        , DIVISION_DESC
        , STORE_ACCOUNT_TYPE_CD
        , EXPRESS_LANE
        , LICENSED_IND
        , RETAILER_SALES_PRICE_PRCNT_BUCKET        
"""


df = sf.snowflake_pull(query=query)
print(df)
