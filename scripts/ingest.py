import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
from urllib.parse import quote_plus
import os

load_dotenv()

# quote_plus handles special characters like @ in passwords
password = quote_plus(os.getenv('DB_PASSWORD'))

DB_URL = f"postgresql://{os.getenv('DB_USER')}:{password}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
engine = create_engine(DB_URL)

RAW_PATH = 'data/raw/'

files = {
    'olist_customers_dataset.csv':      'customers',
    'olist_orders_dataset.csv':         'orders',
    'olist_order_items_dataset.csv':    'order_items',
    'olist_products_dataset.csv':       'products',
    'olist_sellers_dataset.csv':        'sellers',
    'olist_order_payments_dataset.csv': 'order_payments',
    'olist_order_reviews_dataset.csv':  'order_reviews',
}

for filename, table in files.items():
    filepath = RAW_PATH + filename
    print(f'Loading {filename}...')
    df = pd.read_csv(filepath)
    df.to_sql(table, engine, if_exists='replace', index=False)
    print(f'  Loaded {len(df):,} rows into [{table}]')

print('\nAll data loaded successfully!')
