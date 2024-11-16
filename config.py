from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "11caabfc20fca699feff0c24213b1a80")
      API_ID = int(getenv("API_ID", "21527086"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "7399204341:AAEV1MPNDbqF9k3eIi_Q-3k17m5E9mnejHA")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1002087964739:-1002148604082").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
