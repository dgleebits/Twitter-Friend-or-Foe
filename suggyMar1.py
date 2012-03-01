Python 2.7.1 (r271:86832, Jun 16 2011, 16:59:05) 
[GCC 4.2.1 (Based on Apple Inc. build 5658) (LLVM build 2335.15.00)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
>>> 
>>> import tweepy
>>> 
>>> 
>>> 
>>> getState=tweepy.api.get_user('dgleebits').__getstate__()
>>> print getState
{'follow_request_sent': False, 'profile_use_background_image': True, 'id': 364557525, 'verified': False, 'profile_image_url_https': 'https://si0.twimg.com/profile_images/1520153825/1310282366138_normal.jpg', 'profile_sidebar_fill_color': 'DDEEF6', 'profile_text_color': '333333', 'followers_count': 380, 'protected': False, 'location': 'Vancouver BC Canada', 'default_profile_image': False, 'id_str': '364557525', 'status': <tweepy.models.Status object at 0x104b68f90>, 'utc_offset': -28800, 'statuses_count': 1617, 'description': 'I do, what the voices tell me to do. Freelance social media aficionado. Coffee specialist. Internet guru. Thinker. Hacker. White russians - the dude abides.\r\n', 'friends_count': 1995, 'profile_background_image_url_https': 'https://si0.twimg.com/images/themes/theme1/bg.png', 'profile_link_color': '0084B4', 'profile_image_url': 'http://a0.twimg.com/profile_images/1520153825/1310282366138_normal.jpg', 'notifications': False, 'show_all_inline_media': False, 'geo_enabled': False, 'profile_background_color': 'C0DEED', 'profile_background_image_url': 'http://a0.twimg.com/images/themes/theme1/bg.png', 'screen_name': 'DGleebits', 'lang': 'en', 'following': False, 'profile_background_tile': False, 'favourites_count': 24, 'name': 'Dan Gleebits ', 'url': 'http://facebookjustice.wordpress.com', 'created_at': datetime.datetime(2011, 8, 29, 23, 38, 14), 'contributors_enabled': False, 'time_zone': 'Pacific Time (US & Canada)', 'profile_sidebar_border_color': 'C0DEED', 'default_profile': True, 'is_translator': False, 'listed_count': 10}
>>> print getState['url']
http://facebookjustice.wordpress.com
>>> 
