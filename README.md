## python_notion_automation

This repo contains a script for extracting arxiv paper links in twitter likes and extracting them into a reading list notion table

# Key Configuration Setup

To use this repo set up on twitter via:
https://developer.twitter.com/en/portal/dashboard

then add tokens to .env file <br />
api_key='' <br />
api_key_secret='' <br />
bearer_token='' <br />
client_id='' <br />
client_secret='' <br />
twitter_username='' <br />

Then setup notion intergration via:
https://www.notion.so/my-integrations
NOTION_TOKEN='' <br />

Then create a notion table with named columns 'title' (type: title) 'source' (type: url) 'type' (type: multiselect) <br />
(name of columns can be changed / replaced in main file, types are important for 'source') <br />

Then open the table and paste the full url for this <br />
reading_list_url='' <br />

# Installation Setup

conda create -n python_notion_automation python=3.10 <br />
conda activate python_notion_automation <br />
python3 -m pip install -r requirements.txt <br />


