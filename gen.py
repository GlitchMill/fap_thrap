import random
from pornhub_api import PornhubApi
api = PornhubApi()

def gen():

    tags = random.sample(api.video.tags("f").tags, 5)
    category = random.choice(api.video.categories().categories)
    result = api.search.search_videos(ordering="mostviewed", tags=tags, category=category)

    for vid in result:
        link = vid.url
        title = vid.title
        tagsx = vid.tags
        views = vid.views
        cat = vid.categories
        thumb = vid.default_thumb
        break

    return (title,link,tagsx,views,category,thumb)