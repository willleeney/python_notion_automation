## python_notion_automation

This repo contains a script for extracting arxiv paper links in twitter likes and extracting them into a reading list notion table

# Key Configuration Setup

To use this repo set up on twitter via:
https://developer.twitter.com/en/portal/dashboard

then add tokens to .env file
api_key=''
api_key_secret=''
bearer_token=''
client_id=''
client_secret=''
twitter_username=''

Then setup notion intergration via:
https://www.notion.so/my-integrations
NOTION_TOKEN=''

Then create a notion table with named columns 'title' (type: title) 'source' (type: url) 'type' (type: multiselect)
(name of columns can be changed / replaced in main file, types are important for 'source')

Then open the table and paste the full url for this
reading_list_url=''

# Installation Setup

conda create -n python_notion_automation python=3.10
conda activate python_notion_automation
python3 -m pip install -r requirements.txt


