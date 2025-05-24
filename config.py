import re
import os
from os import environ
from Script import script

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default
      
# Bot Information
API_ID = int(environ.get("API_ID", "28519661"))
API_HASH = environ.get("API_HASH", "d47c74c8a596fd3048955b322304109d")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

PICS = (environ.get('PICS', 'https://graph.org/file/2518d4eb8c88f8f669f4c.jpg https://graph.org/file/d6d9d9b8d2dc779c49572.jpg https://graph.org/file/4b04eaad1e75e13e6dc08.jpg https://graph.org/file/05066f124a4ac500f8d91.jpg https://graph.org/file/2c64ed483c8fcf2bab7dd.jpg')).split() # Bot Start Picture
FORCESUB_IMG = os.environ.get("FORCESUB_IMG", "https://telegra.ph/file/e292b12890b8b4b9dcbd1.jpg")
BAN_SUPPORT = os.environ.get("BAN_SUPPORT", "https://t.me/Spideyofficial_777")
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '5518489725 7965267063').split()]
BOT_USERNAME = environ.get("BOT_USERNAME", "") # without @
PORT = environ.get("PORT", "8080")

# Clone Info :-
CLONE_MODE = bool(environ.get('CLONE_MODE', False)) # Set True or False
 
# If Clone Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
CLONE_DB_URI = environ.get("CLONE_DB_URI", "")
CDB_NAME = environ.get("CDB_NAME", "cloneSpidey")

# Database Information
DB_URI = environ.get("DB_URI", "mongodb+srv://Soldier:QTo6GiCGk4xQTRRw@cluster0.igba5fh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = environ.get("DB_NAME", "spideyofficial")

# Auto Delete Information
AUTO_DELETE_MODE = bool(environ.get('AUTO_DELETE_MODE', True)) # Set True or False

# If Auto Delete Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
AUTO_DELETE = int(environ.get("AUTO_DELETE", "15")) # Time in Minutes
AUTO_DELETE_TIME = int(environ.get("AUTO_DELETE_TIME", "1800")) # Time in Seconds
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 7200))
FSUB_LINK_EXPIRY = int(os.getenv("FSUB_LINK_EXPIRY", "10"))  # 0 means no expiry
#for the forceSub channel id's
MULTI_FSUB = [int(channel_id) for channel_id in environ.get('MULTI_FSUB', '-1001959922658 -1002433552221 -1002470391435').split() if re.match(r'^-?\d+$', channel_id)] 
# Channel Information
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002294764885"))
VERIFIED_LOG = int(environ.get('VERIFIED_LOG', '-1002423451263')) 
VERIFY = bool(environ.get('VERIFY', True))  # Verification On (True) / Off (False)
VERIFY_EXPIRE = int(environ.get('VERIFY_EXPIRE', 5))  # Add time in hours
HOW_TO_VERIFY = environ.get('HOW_TO_VERIFY', 'https://t.me/spideyofficial_777/12')  # How to open tutorial link for verification
auth_channel = environ.get('AUTH_CHANNEL', '-1001959922658')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None

# File Caption Information
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)

# Enable - True or Disable - False
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

# Verify Info :-
VERIFY_MODE = bool(environ.get('VERIFY_MODE', True)) # Set True or False

# If Verify Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
SHORTLINK_URL = environ.get("SHORTLINK_URL", "shortxlinks.com") # shortlink domain without https://
SHORTLINK_API = environ.get("SHORTLINK_API", "09c3f9bc3a8b121b1e6b82a954e59da523dd188e") # shortlink api
VERIFY_TUTORIAL = environ.get("VERIFY_TUTORIAL", "https://t.me/SPIDEYOFFICIAL_777/12") # how to open link 

# Website Info:
WEBSITE_URL_MODE = bool(environ.get('WEBSITE_URL_MODE', True)) # Set True or False

# If Website Url Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
WEBSITE_URL = environ.get("WEBSITE_URL", "https://spideyzshortner.netlify.app/") # For More Information Check Video On Yt - @Tech_VJ

# File Stream Config
STREAM_MODE = bool(environ.get('STREAM_MODE', True)) # Set True or False

# If Stream Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
URL = environ.get("URL", "https://vj-file-store-podr.onrender.com/")
