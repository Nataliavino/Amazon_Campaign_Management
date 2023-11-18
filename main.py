import datetime
from get_amazon_data import CampaignData, CampaignUpdater
from get_token import AccessToken
import time
from config import REFRESH_TOKEN, CAMPAIGN1_ID, CAMPAIGN2_ID


start_date = str(datetime.datetime.now())[:10]


# Get access token
ACCESS_TOKEN = AccessToken(REFRESH_TOKEN).get_access_token()
campaign_data = CampaignData(ACCESS_TOKEN)
campaign_updater = CampaignUpdater(ACCESS_TOKEN)

# Get list of campaigns
list_camp = campaign_data.get_list_campaign()['campaigns']

list_camp_id = [CAMPAIGN1_ID, CAMPAIGN2_ID]

# Update the status of campaigns from the list
for camp_id in list_camp_id:
    for camp in list_camp:
        if camp['campaignId'] == camp_id:
            if camp['state'] == "ENABLED":
                campaign_updater.update_status_campaign(camp_id, "PAUSED")
            else:
                campaign_updater.update_status_campaign(camp_id, "ENABLED")
            time.sleep(3)

