from json import JSONDecodeError

import pandas as pd
import warnings
import re
import urllib.request
import json

warnings.filterwarnings('ignore')

def review_parsing(id):
    url = f'https://api.kinolights.com/v1/movie/{id}/reviews?sort_filter=review_like_desc'
    # review_dict = requests.get(url).text
    req = urllib.request.Request(url)
    #### get data & json format
    data_get = urllib.request.urlopen(req).read()
    try:
        review_jsons = json.loads(data_get)['data']
        reviews_df = pd.DataFrame(review_jsons)
        reviews_df = reviews_df.drop(
            ['Idx', 'ReviewLink', 'IsPrivate', 'ReviewLength', 'Me_Like', 'User_IndexRating', 'Movie_ProductionYear',
             'User_IsPremium',
             'CreatedAt', 'ProfileImageUrl', 'PosterImageUrl', 'UserIdx'], axis=1)
        reviews_df.rename(columns={'MovieIdx': 'KinoId', 'Movie_TitleKr': 'TitleKr', 'UserName': 'User'}, inplace=True)
        #이모지제거
        reviews_df["ReviewTitle"] = reviews_df["ReviewTitle"].str.replace(pat=r'[^\w\s]', repl=r'', regex=True)
        reviews_df["Review"] = reviews_df["Review"].str.replace(pat=r'[^\w\s]', repl=r'', regex=True)
    except:
        print(f'리뷰가 없습니다.')
        return None
    return reviews_df