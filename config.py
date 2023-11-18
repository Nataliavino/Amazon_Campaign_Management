import os

# Amazon Advertising API credentials
CLIENT_ID = os.environ.get('client_id')
CLIENT_SECRET = os.environ.get('client_secret')
PROFILE_ID = os.environ.get('profile_id')
PORTFOLIO_ID = os.environ.get('portfolio_id')
CAMPAIGN1_ID = os.environ.get('camp1_id')
CAMPAIGN2_ID = os.environ.get('camp2_id')
REFRESH_TOKEN = os.environ.get('refresh_token')

# API URLs
TOKEN_URL = 'https://api.amazon.com/auth/o2/token'
CAMPAIGN_URL = 'https://advertising-api.amazon.com/sp/campaigns'

