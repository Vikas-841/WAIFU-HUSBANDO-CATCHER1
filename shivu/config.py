class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "5932230962"
    sudo_users = "5932230962", "5778743582", "5396889141", "5852831718", "6375797149"
    GROUP_ID = -1002135424353
    TOKEN = "6744789477:AAH5XfBj4mVGwZHraxeAEPD66Ty_nJJ3eiA"
    mongo_url = "mongodb+srv://edit72160:edit72160@cluster0.aceg9xy.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "VG_SUPPORT_CHAT"
    UPDATE_CHAT = "TEAMS_VG"
    BOT_USERNAME = "sexy_waifu_bot"
    CHARA_CHANNEL_ID = "-1002135424353"
    api_id = 26626068
    api_hash = "bf423698bcbe33cfd58b11c78c42caa2"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
