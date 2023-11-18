import requests
from config import CLIENT_ID, PROFILE_ID, CAMPAIGN_URL, PORTFOLIO_ID


class CampaignData:
    def __init__(self, token):
        self.token = token
        self.header = {
            'Amazon-Advertising-API-ClientId': CLIENT_ID,
            'Authorization': f'{self.token}',
            'Amazon-Advertising-API-Scope': PROFILE_ID,
            'Accept': 'application/vnd.spCampaign.v3+json',
            'Content-Type': 'application/vnd.spCampaign.v3+json'
        }

    def get_list_campaign(self):
        # Send a POST request to get list of campaigns
        try:
            response = requests.post(f'{CAMPAIGN_URL}/list', headers=self.header)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error getting list of campaigns: {e}")


class CampaignUpdater:
    def __init__(self, token):
        self.token = token
        self.header = {
            'Amazon-Advertising-API-ClientId': CLIENT_ID,
            'Authorization': f'{self.token}',
            'Amazon-Advertising-API-Scope': PROFILE_ID,
            'Accept': 'application/vnd.spCampaign.v3+json',
            'Content-Type': 'application/vnd.spCampaign.v3+json'
        }

    def update_status_campaign(self, camp_id, status):
        # Set data to update the campaign status
        data = {
            "campaigns": [
                    {
                        "portfolioId": PORTFOLIO_ID,
                        "campaignId": camp_id,
                        "state": status,
                    }]}

        # Send a PUT request update the campaign status
        try:
            response = requests.put(CAMPAIGN_URL, headers=self.header, json=data)
            response.raise_for_status()
            print(response.status_code)
        except requests.exceptions.RequestException as e:
            print(f"Error updating status: {e}")
