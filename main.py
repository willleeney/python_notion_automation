import tweepy
from decouple import config
import urllib
import re
import arxiv
import pandas as pd
import notion_df

notion_df.pandas()
notion_df.config(api_key=config('NOTION_TOKEN'))
page_url = config('reading_list_url')

def run():
    # get notion table to update to
    df_download = pd.read_notion(page_url, resolve_relation_values=True)

    # get twitter data
    client = tweepy.Client(
        bearer_token=config('bearer_token'),
        consumer_key=config('client_id'),
        consumer_secret=config('client_secret'),
        access_token=config('api_key'),
        access_token_secret=config('api_key_secret'),
        wait_on_rate_limit=True
    )

    response = client.get_user(username=config('twitter_username'))
    user_id = response.data.data['id']
    response = client.get_liked_tweets(user_id,
                                       max_results=100,
                                       tweet_fields=["attachments", "context_annotations"])

    get_tweets = 1
    while get_tweets != 0:

        for tweet in response.data:
            # TO DO - doesn't search sub tweets
            tweet_urls = re.findall("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", tweet.text)
            if not tweet_urls:
                continue
            for url in tweet_urls:
                try:
                    opener = urllib.request.build_opener()
                    request = urllib.request.Request(url)
                    url_response = opener.open(request)
                    actual_url = url_response.geturl()
                    extracted_url = str(actual_url)
                except:
                    extracted_url = str(url)

                # only finds arxiv results
                if 'arxiv' not in extracted_url:
                    continue
                else:
                    print(f'link_to_paper: {extracted_url}')
                    search_id = extracted_url.split("https://arxiv.org/abs/")[1]
                    paper = next(arxiv.Search(id_list=[search_id]).results())
                    title = paper.title

                if set([title]).issubset(df_download['title']):
                    get_tweets = 0
                    break
                else:
                    print(f'Uploading to Notion: {title}')
                    new_df = pd.DataFrame({
                        'title': title,
                        'source': extracted_url,
                        'type': ['research paper']})

                    new_df.to_notion(page_url, resolve_relation_values=True)
                    #filename = f'{title}.pdf'
                    #paper.download_pdf(dirpath="./papers", filename=filename)

            if get_tweets == 0:
                break
            else:
                if response.meta['result_count'] != 0:
                    response = client.get_liked_tweets(user_id,
                                                       max_results=100,
                                                       pagination_token=response.meta['next_token'],
                                                       tweet_fields=["attachments", "context_annotations"])

    return

if __name__ == '__main__':
    run()
