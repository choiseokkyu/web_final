```
$pip install google-cloud-bigquery
```

```
$pip install pandas-gbq
```

```
export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/[FILE_NAME].json"
```

```
from google.cloud import bigquery

client = bigquery.Client.from_service_account_json(
    'path/to/service_account.json')
```
