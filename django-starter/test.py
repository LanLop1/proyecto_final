#%%

from decouple import config
import re

db_url = config('DB_URL')
safe_db_url = re.sub(r':.*@', ':****@', db_url)
print(f"DB_URL: {safe_db_url}")