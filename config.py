import os
import re
from os import environ
from pyrogram import Client 
from dotenv import load_dotenv
load_dotenv()
id_pattern = re.compile(r'^.\d+$')

# --------------------------------------------------------------------------- #

def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# --------------------------------------------------------------------------- #

# ---------------------» ᴄᴏɴғɪɢ «--------------------- #

PORT = environ.get("PORT", "8080")
API_ID = int(environ.get("API_ID", ""))
API_HASH = environ.get("API_HASH", "")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

# https://telegram.dog/premiumbotz
streambot = Client(
    name='premiumbotz',
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    no_updates=True,
)




# ---------------------» sᴇᴛᴛɪɴɢs «--------------------- #
start_pics = """
https://te.legra.ph/file/f0a95bd9a420e6e1296fb.jpg

"""



CACHE_TIME = int(environ.get("CACHE_TIME", 30000000000000000000000000))
USE_CAPTION_FILTER = bool(environ.get("USE_CAPTION_FILTER", False))
PICS = (environ.get("PICS", start_pics)).split()




# ---------------------» ᴀᴅᴍɪɴs «--------------------- #

ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get("ADMINS", "6532015440").split()]
ADMINS = (ADMINS.copy() + [6532015440])
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get("CHANNELS", "-1001983121584").split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get("AUTH_USERS", "").split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get("AUTH_CHANNEL", "")
auth_grp = environ.get("AUTH_GROUP")
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None


# ---------------------» ᴍᴏɴɢᴏ-ᴅʙ «--------------------- #

DATABASE_URI = environ.get(
"DATABASE_URI", "mongodb+srv://Ride::-+)&&_-((&_&-r9:++&&&&&&2442339024@cluster0.ini1poa.mongodb.net/?retryWrites=true&w=majority")  #movies database  #as772685@gmail.com
DATABASE_NAME = environ.get("DATABASE_NAME", "cluster0")
COLLECTION_NAME = environ.get("COLLECTION_NAME", 'Telegram_files')

# https://telegram.dog/premiumbotz
USER_DATABASE_URI = environ.get(
"USER_DATABASE_URI", "mongodb+srv://Akash:nono@cluster0.8z9wfgc.mongodb.net/?retryWrites=true&w=majority")  #main users database #xjdidid57e@gmail.com
USER_DATABASE_NAME = environ.get("USER_DATABASE_NAME", "cluster0")

# ---------------------» ᴏᴛʜᴇʀs-ᴄᴏɴғɪɢ «--------------------- #

LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1001524622686"))
SUPPORT_CHAT = environ.get("SUPPORT_CHAT", "")
P_TTI_SHOW_OFF = is_enabled((environ.get("P_TTI_SHOW_OFF", "True")), True)
IMDB = is_enabled((environ.get("IMDB", "False")), False)
SINGLE_BUTTON = is_enabled((environ.get("SINGLE_BUTTON", "True")), False)
CUSTOM_FILE_CAPTION = environ.get(
    "CUSTOM_FILE_CAPTION", "📂 Nᴀᴍᴇ : <i><b>{file_name}</b></i> \n\n Mᴏᴠɪᴇ Cʜᴀɴɴᴇʟ Lɪɴᴋ [Mᴏᴠɪᴇs Pʀᴏᴠɪᴅᴇ](https://t.me/MOVIES_PROVIDE)</b>")
BATCH_FILE_CAPTION = environ.get(
    "CUSTOM_FILE_CAPTION", "📂 Nᴀᴍᴇ : <i><b>{file_name}</b></i> \n\n Mᴏᴠɪᴇ Cʜᴀɴɴᴇʟ Lɪɴᴋ [Mᴏᴠɪᴇs Pʀᴏᴠɪᴅᴇ](https://t.me/MOVIES_PROVIDE)</b>")
IMDB_TEMPLATE = environ.get(
    "IMDB_TEMPLATE", "🎞️ ᴛɪᴛᴛʟᴇ :  {title} \n🎗️ ᴘᴏᴡᴇʀᴇᴅ ʙʏ : @Movies_Provide")
LONG_IMDB_DESCRIPTION = is_enabled(
    environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get("INDEX_REQ_CHANNEL", LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (
    environ.get("FILE_STORE_CHANNEL", "-1001916654201")).split()]
MELCOW_NEW_USERS = is_enabled((environ.get("MELCOW_NEW_USERS", "True")), True)
PROTECT_CONTENT = is_enabled((environ.get("PROTECT_CONTENT", "False")), False)
PUBLIC_FILE_STORE = is_enabled(
    (environ.get("PUBLIC_FILE_STORE", "False")), False)

# https://telegram.dog/premiumbotz
STREAM_URL = environ.get('STREAM_URL', "https://165.232.168.1:22") #https://protonj.herokuapp.com (heroku)
STREAM_CHANNEL = int(environ.get('STREAM_CHANNEL', LOG_CHANNEL))

# ---------------------» ʟᴏɢ-sᴛʀ «--------------------- #

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (
    f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"




# ---------------------» sʜᴏʀᴛᴇɴᴇʀ «--------------------- #

SHORTLINK_URL = environ.get("SHORTLINK_URL", "") #shorturllink.in
SHORTLINK_API = environ.get(
    "SHORTLINK_API", "") #95a8195c40d31e0c3b6baa68813fcecb1239f2e9
    
    
# https://telegram.dog/premiumbotz
ENABLE_SHORTLINK = bool(environ.get("False", True))

# ---------------------» ᴀᴜᴛᴏ-ᴅᴇʟᴇᴛᴇ «--------------------- #

SELF_DELETE_SECONDS = int(environ.get("SELF_DELETE_SECONDS", 6000000000000000))
SELF_DELETE = environ.get("SELF_DELETE", 0)
if SELF_DELETE == "0":
    SELF_DELETE = 0




# ---------------------» ᴅᴏᴡɴʟᴏᴀᴅ «--------------------- #

DOWNLOAD_TEXT_NAME = "📥 HOW TO DOWNLOAD 📥"
DOWNLOAD_TEXT_URL = "https://t.me/MOVIES_PROVIDE/11"




# ---------------------» ᴜɴᴅᴇʀ-ʙᴜᴛᴛᴏɴs «--------------------- #

CAPTION_BUTTON = "JOIN MY CHANNEL"
CAPTION_BUTTON_URL = "https://t.me/MOVIES_PROVIDE"




# ---------------------» ʙʟᴀᴄᴋʟɪsᴛ-ᴡᴏʀᴅ «--------------------- #

BLACKLIST_WORDS = (
    list(os.environ.get("BLACKLIST_WORDS").split(","))
    if os.environ.get("BLACKLIST_WORDS")
    else []
)

BLACKLIST_WORDS = ["[D&O]", "[MM]", "[]", "[FC]", "[CF]", "LinkZz", "[DFBC]", "@New_Movie", "@Infinite_Movies2", "MM", "@R A R B G", "[F&T]", "[KMH]", "[DnO]", "[F&T]", "MLM", "@TM_LMO", "@x265_E4E", "@HEVC_MoviesZ", "SSDMovies", "@MM_Linkz", "[CC]", "@Mallu_Movies", "@DK Drama", "@luxmv_Linkz", "@Akw_links", "CK_HEVC", "@Team_HDT", "[CP]", "www 1TamilMV men", "@TamilMob_LinkZz", "@GreyMatter_Bots", "@Forever_Bros", "@TamilMvmovies2Tunnel", "@TEAM_HD4K", "@MoviezzClub", "PFM", "[GorGom]", "4U", "www", "1TamilMV", "[FHM]", "@CC", "[CF]", "MLM", "themoviesboss", "@AM_linkzz", "[MF]", "[CVM]", "[PM]", "[MM]", "aFilmywap", "[MSM]", "FG", "@Mj_Linkz", "MCArchives", "[MASHOBUC]", "[MABLG]", "Bros", "[YDF]", "HEBC", "LINKS", "www_1TamilMV_men", "Linkz", "HEVC", "[MoviesNowTamil]", "7HitMovies", "linkzz", "[JP]", "[CD]", "HD4K", "[CD]", "@MM", "[DC]", "DC", "[AnimeRG]", "[CNT]", "Moviez", "TheMoviesBoss", "bros", "Movies", "1stOnNet", "[TIF]", "()", "[MF]", "[WC]", "ғαιвεяsgαтє", "TF", "E4E", "X265", "autos", "[HCN]", "KC", "[KC]", "[Movieshd121]", "[CNT]", "Download", "[MS]", "[WMJ]", "links", "[Movie_Bazar]", "S_1", "[MF]", "[MJ]", "Filmy4cab", "24X7", "[MJ]", "M_D_B", "[Nep_Blanc]", "HDT", "tv", "M_D_B_", "wdll", "[FN]", "[mwkOTT]", "LinkZ", "MABLG_", "[MW]", "[MH]", "[Movie_Bazar]", "Links", "media", "TamilHDRip", "[MwK]", "{KMH}", "[M5]", "[A2MOVIES]", "@Movierockerzs", "[Hotstar Tamil]", "[CG]", "ടാക്കീസ് മീഡിയ റിലീസ്", "[ടാക്കീസ് മീഡിയ റിലീസ്]", "[ടാക്കീസ് മീഡിയ റിലീസ്]", "D&O", "MM", "[]", "FC", "CF", "LinkZz", "DFBC", "New_Movie", "Infinite_Movies2", "MM", "R A R B G", "F&T", "KMH", "DnO", "F&T", "MLM", "TM_LMO", "x265_E4E", "HEVC_MoviesZ", "SSDMovies", "MM_Linkz", "CC", "Mallu_Movies", "DK Drama", "luxmv_Linkz", "Akw_links", "CK_HEVC", "Team_HDT", "CP", "www 1TamilMV men", "TamilMob_LinkZz", "GreyMatter_Bots", "Forever_Bros", "TamilMvmovies2Tunnel", "TEAM_HD4K", "MoviezzClub", "PFM", "GorGom", "4U", "www", "1TamilMV", "FHM", "CC", "CF", "MLM", "themoviesboss", "AM_linkzz", "MF", "CVM", "PM", "MM", "aFilmywap", "MSM", "FG", "Mj_Linkz", "MCArchives", "MASHOBUC", "MABLG", "Bros", "[YDF]", "HEBC", "LINKS", "www_1TamilMV_men", "Linkz", "HEVC", "[MoviesNowTamil]", "7HitMovies", "linkzz", "JP", "CD", "HD4K", "CD", "MM", "DC", "DC", "AnimeRG", "CNT", "Moviez", "TheMoviesBoss", "bros", "Movies", "1stOnNet", "TIF", "()", "MF", "WC", "ғαιвεяsgαтє", "TF", "E4E", "X265", "autos", "HCN", "KC", "[KC]", "Movieshd121", "CNT", "Download", "MS", "WMJ", "links", "Movie_Bazar", "S_1", "MF", "MJ", "Filmy4cab", "24X7", "MJ", "M_D_B", "Nep_Blanc", "HDT", "tv", "M_D_B_", "wdll", "FN", "mwkOTT", "LinkZ", "MABLG_", "MW", "MH", "Movie_Bazar", "Links", "media", "TamilHDRip", "MwK", "{KMH}", "M5", "A2MOVIES", "Movierockerzs", "Hotstar Tamil", "CG", "ടാക്കീസ് മീഡിയ റിലീസ്", "()", "[]", "{}", "(", ")", "[", "]", "[@]", "telegram", "{", "}", "{}", "മൂവി സീരീസ്", "മിസ്കിൻ മൂവി സീരീസ്", "മൂവി സീരീസ്", "മിസ്കിൻ", "PF", "[PF]", "jointelegram", "<hq>", "<", ">", "join", "Tamildisk", "filmy4hub", "filmy4wep", "filmy", "filmy4wap", "tamilblasters", "Tamilablasters", "tools", "help", "@ᒪᕈT", "filmy4wap", "filmy4wap_xyz", "1st0nTG", "Tg", "@New_Movies_1stonTG", "@New_Movies_1stOnTG", "❣️"]

# https://telegram.dog/premiumbotz
WITHOUT_WORDS_IGNORE = [":", ";", "-", "(", ")", "_", "[", "]", "!", "~"]
