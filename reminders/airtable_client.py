from typing import List, Dict
import requests


class AirtableClient:
    def __init__(self, sheet_url: str, api_key: str):
        self.sheet_url = sheet_url
        self.default_headers = {
            'Authorization': 'Bearer ' + api_key,
            'Content-Type': 'application/json'
        }

    def update_record(self, airtable_record_id: str, attributes: Dict):
        resp = requests.patch(self.sheet_url + '/' + airtable_record_id,
                              headers=self.default_headers,
                              json={'fields': attributes})

    def get_records(self):
        return requests.get(self.sheet_url, headers=self.default_headers)
