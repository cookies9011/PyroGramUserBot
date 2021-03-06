import os

class Config(object):
    LOGGER = True
    # The Telegram API things
    APP_ID = int(os.environ.get("APP_ID", 1045417)
    API_HASH = os.environ.get("API_HASH", 103c70750fdb97721ff6523fed3c8ec0)
    # Get these values from my.telegram.org
    # string session for running on Heroku
    # some people upload their session files on GitHub or other third party hosting
    # websites, this might prevent the un-authorized use of the
    # confidential session files
    HU_STRING_SESSION = os.environ.get("HU_STRING_SESSION", BACa_ApzkjiJj3eKEOzsTOoIFty2bRIfMyqxN0f8ynXJ29qR2GY24BfOORFynjThjAO5v_daEZu65ORI6W1Sd_BhH9NZuf4RtETn8eouYtD43wnK6mmCFtMkipkEwDHMFuk4xXSs855AUYIQSfTC29gJ1ystTK3DVbVYuic0nxgzahVmDRbTeNNkcy7D1uYu5myfgXWlndn8EbUxLfbrXReSEEMA2VUYaX1m_Sm4P4E2FRDRRdm6UKzCHK2VToy0WvVrpkGjETgPOJZpWSarDoAGM08FQMUp6wgw7-grRaN0I0YkmIfMM6X9ikj3VYzCPX0kMJNsBuZPiWPciRV_qbgYNr9yzAA)
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # specify command handler that should be used for the plugins
    # this should be a valid "regex" pattern
    COMMAND_HAND_LER = os.environ.get("COMMAND_HAND_LER", ".")
    # This is required for the plugins involving the file system.
    TMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY", "./DOWNLOADS/")
    # get a Heroku API key from http://dashboard.heroku.com/account
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
    # set this to your fork on GitHub (if you want)
    OFFICIAL_UPSTREAM_REPO = os.environ.get("OFFICIAL_UPSTREAM_REPO", "https://github.com/SpEcHiDe/PyroGramUserBot")
    # For Databases
    # can be None in which case plugins requiring
    # DataBase would not work
    DB_URI = os.environ.get("DATABASE_URL", None)
    # gDrive variables
    G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
    G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
