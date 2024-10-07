import requests
import json

class MantisBugTracker:

    def __init__(self, projectId):
        self.project_id = projectId

    def log_issue(self, summary, description):
        url = "http://localhost/mantisbt-2.26.2/api/rest/issues"
        payload = json.dumps(
            {
                "summary": summary,
                "description": description,
                "project": {
                    "id": self.project_id
                },
                "category": {
                    "id": 1
                },
                "priority": {
                    "name": "normal"
                },
                "severity": {
                    "name": "trivial"
                },

                "reproducibility": {
                    "name": "always"
                }
            }
        )
        headers = {
            'Authorization': 'oUoksqROt2h9ivjiqw7sTA8S41G8ChLv',
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)