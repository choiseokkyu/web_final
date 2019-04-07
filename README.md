<p>path 설정</p>
```
export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/[FILE_NAME].json"
```
<p>or</p>
```
from google.cloud import bigquery

client = bigquery.Client.from_service_account_json(
    'path/to/service_account.json')
```
