import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# ------------------------------------------------------------- #

def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# ---------------------» sᴄʀɪᴘᴛ-ᴄʟᴀss «--------------------- #

class script(object):
    HOME_BUTTONURL_UPDATES = environ.get(
        "HOME_BUTTONURL_UPDATES", 'https://t.me/Rexisop99')
    START_TXT = environ.get("START_TXT", """

ʜᴇʟʟᴏ {} ✨

ɪ ᴀᴍ ɴᴇxᴛ ɢᴇɴᴇʀᴀᴛɪᴏɴ ᴀᴅᴠᴀɴᴄᴇᴅ ᴀᴜᴛᴏ ғɪʟᴛᴇʀ ᴡɪᴛʜ ʟɪɴᴋ sʜᴏʀᴛᴇɴᴇʀ ʙᴏᴛ

ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴀꜱ ᴀᴜᴛᴏ ғɪʟᴛᴇʀ ᴡɪᴛʜ ʟɪɴᴋsʜᴏʀᴛᴇɴᴇʀ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ
ɪᴛꜱ ᴇᴀꜱʏ ᴛᴏ ᴜꜱᴇ ᴊᴜꜱᴛ ᴀᴅᴅ ᴍᴇ ᴀꜱ ᴀᴅᴍɪɴ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ɪ ᴡɪʟʟ ᴘʀᴏᴠɪᴅᴇ ᴛʜᴇʀᴇ ᴍᴏᴠɪᴇꜱ ᴡɪᴛʜ ʏᴏᴜʀ ʟɪɴᴋꜱʜᴏʀᴛᴇɴᴇʀ
""")



# ---------------------» ʜᴇʟᴘ-ᴛᴇxᴛ «--------------------- #

    HELP_TXT = """ʜᴇʏ {}
ʜᴇʀᴇ ɪs ʜᴇʟᴘ sᴇᴄᴛɪᴏɴ. ."""
    ABOUT_TXT = """<b>ᴀʙᴏᴜᴛ ᴍᴇ <i>🤖 ᴍʏ ɴᴀᴍᴇ : <a href=https://t.me/><b>Rᴀᴍʙᴏ</b></a>\n
👨‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href=https://t.me/Rexisop99><b>Rᴀᴍʙᴏ</b></a>\n
📝 ʟᴀɴɢᴜᴀɢᴇ : ᴘʏʀᴏɢʀᴀᴍ\n
📚 ꜰʀᴀᴍᴇᴡᴏʀᴋ : ᴘʏᴛʜᴏɴ 3\n
📡 ʜᴏsᴛᴇᴅ ᴏɴ : ʜᴇʀᴏᴋᴜ\n
📢 ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/MOVIES_PROVIDE><b></b>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>\n
🌟 ᴠᴇʀsɪᴏɴ : ᴠ 4.0\n</b></i>"""



# ---------------------» sᴏᴜʀᴄᴇ-ᴛᴇxᴛ «--------------------- #

    SOURCE_TXT = """<b>ᴄʀᴇᴀᴛᴇ ᴏɴᴇ ʟɪᴋᴇ ᴛʜɪs:</b>
• ᴡᴀɴᴛ ᴛᴏ ʀᴇᴘᴏ ᴏғ ᴛʜɪs ʙᴏᴛ ʙᴜᴅᴅʏ !! <b>
• ᴄᴏɴᴛᴀᴄᴛ - [ʀᴀᴍʙᴏ](t.me/Rexisop99)<b>"""



# ---------------------» ᴍᴀɴᴜᴀʟ-ғɪʟᴛᴇʀs «--------------------- #

    MANUELFILTER_TXT = """ʜᴇʟᴘ : <b>ғɪʟᴛᴇʀs</b>

- ғɪʟᴛᴇʀ ɪs ᴛʜᴇ ғᴇᴀᴛᴜʀᴇ ᴡᴇʀᴇ ᴜsᴇʀs ᴄᴀɴ sᴇᴛ ᴀᴜᴛᴏᴍᴀᴛᴇᴅ ʀᴇᴘʟɪᴇs ғᴏʀ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴋᴇʏᴡᴏʀᴅ ᴀɴᴅ sᴇᴀʀᴄʜ ʙᴏᴛ ᴡɪʟʟ ʀᴇsᴘᴏɴᴅ ᴡʜᴇɴᴇᴠᴇʀ ᴀ ᴋᴇʏᴡᴏʀᴅ ɪs ғᴏᴜɴᴅ ᴛʜᴇ ᴍᴇssᴀɢᴇ

<b>ɴᴏᴛᴇ:</b>
1. sᴇᴀʀᴄʜ ʙᴏᴛ sʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟʟᴀɢᴇ.
2. ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴀᴅᴅ ғɪʟᴛᴇʀs ɪɴ ᴀ ᴄʜᴀᴛ.
3. ᴀʟᴇʀᴛ ʙᴜᴛᴛᴏɴs ʜᴀᴠᴇ ᴀ ʟɪᴍɪᴛ ᴏғ 64 ᴄʜᴀʀᴀᴄᴛᴇʀs.

<b>ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ᴜsᴀɢᴇ:</b>
• <code>/filter</code> - <code>ᴀᴅᴅ ᴀ ғɪʟᴛᴇʀ ɪɴ ᴄʜᴀᴛ</code>
• <code>/filters</code> - <code>ʟɪsᴛ ᴀʟʟ ᴛʜᴇ ғɪʟᴛᴇʀs ᴏғ ᴀ ᴄʜᴀᴛ</code>
• <code>/del</code> - <code>ᴅᴇʟᴇᴛᴇ ᴀ sᴘᴇᴄɪғɪᴄ ғɪʟᴛᴇʀ ɪɴ ᴄʜᴀᴛ</code>
• <code>/delall</code> - <code>ᴅᴇʟᴇᴛᴇ ᴛʜᴇ ᴡʜᴏʟᴇ ғɪʟᴛᴇʀs ɪɴ ᴀ ᴄʜᴀᴛ (ᴄʜᴀᴛ ᴏᴡɴᴇʀ ᴏɴʟʏ)</code>"""



# ---------------------» ʙᴜᴛᴛᴏɴ-ᴛᴇxᴛ «--------------------- #

    BUTTON_TXT = """ʜᴇʟᴘ : <b>ʙᴜᴛᴛᴏɴs</b>

- sᴇᴀʀᴄʜ ʙᴏᴛ sᴜᴘᴘᴏʀᴛs ʙᴏᴛʜ ᴜʀʟ ᴀɴᴅ ᴀʟᴇʀᴛ ɪɴʟɪɴᴇ ʙᴜᴛᴛᴏɴs.

<b>ɴᴏᴛᴇ:</b>
1. ᴛᴇʟᴇɢʀᴀᴍ ᴡɪʟʟ ɴᴏᴛ ᴀʟʟᴏᴡs ʏᴏᴜ ᴛᴏ sᴇɴᴅ ʙᴜᴛᴛᴏɴs ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴄᴏɴᴛᴇɴᴛ, sᴏ ᴄᴏɴᴛᴇɴᴛ ɪs ᴍᴀɴᴅᴀᴛᴏʀʏ.
2. sᴇᴀʀᴄʜ ʙᴏᴛ sᴜᴘᴘᴏʀᴛs ʙᴜᴛᴛᴏɴs ᴡɪᴛʜ ᴀɴʏ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴇᴅɪᴀ ᴛʏᴘᴇ.
3. ʙᴜᴛᴛᴏɴs sʜᴏᴜʟᴅ ʙᴇ ᴘʀᴏᴘᴇʀʟʏ ᴘᴀʀsᴇᴅ ᴀs ᴀᴍʀᴋᴅᴏᴡɴ ғᴏʀᴍᴀᴛ.

<b>ᴜʀʟ ʙᴜᴛᴛᴏɴs:</b>
<code>[Button Text](buttonurl:https://t.me/cyofficial)</code>

<b>ᴀʟᴇʀᴛ ʙᴜᴛᴛᴏɴs:</b>
<code>[Button Text](buttonalert:ᴛʜɪs ɪs ᴀɴ ᴀʟᴇʀᴛ ᴍᴇssᴀɢᴇ)</code>"""



# ---------------------» ᴀᴜᴛᴏ-ғɪʟᴛᴇʀs «--------------------- #

    AUTOFILTER_TXT = """ʜᴇʟᴘ : <b>ᴀᴜᴛᴏ ғɪʟᴛᴇʀs</b>

<b>ɴᴏᴛᴇ:</b>
1. ᴍᴀᴋᴇ ᴍᴇ ᴛʜᴇ ᴀᴅᴍɪɴ ᴏғ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ɪғ ɪᴛ's ᴘʀɪᴠᴀᴛᴇ.
2. ᴍᴀᴋᴇ sᴜʀᴇ ᴛʜᴀᴛ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴅᴏᴇs ɴᴏᴛ ᴄᴏɴᴛᴀɪɴs ᴄᴀᴍʀɪᴘs, ᴘᴏʀ ᴀɴᴅ ғᴀᴋᴇ ғɪʟᴇs.
3. ғᴏʀᴡᴀʀᴅ ᴛʜᴇ ʟᴀsᴛ ᴍᴇssᴀɢᴇ ᴛᴏ ᴍᴇ ᴡɪᴛʜ ǫᴜᴏᴛᴇs.
 ɪ'ʟʟ ᴀᴅᴅ ᴀʟʟ ᴛʜᴇ ғɪʟᴇs ɪɴ ᴛʜᴀᴛ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴍʏ ᴀᴛᴀʙᴀsᴇ."""



# ---------------------» ᴄᴏɴɴᴇᴄᴛɪᴏɴ-ᴛᴇxᴛ «--------------------- #

    CONNECTION_TXT = """ʜᴇʟᴘ : <b>ᴄᴏɴɴᴇᴄᴛɪᴏɴs</b>

- ᴜsᴇᴅ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʙᴏᴛ ᴛᴏ ᴘᴍ ғᴏʀ ᴍᴀɴᴀɢɪɴɢ ғɪʟᴛᴇʀs. 
- ɪᴛ ʜᴇʟᴘs ᴛᴏ ᴀᴠᴏɪᴅ sᴘᴀᴍᴍɪɴɢ ɪɴ ɢʀᴏᴜᴘs.

<b>ɴᴏᴛᴇ:</b>
1. ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴀᴅᴅ ᴀ ᴄᴏɴɴᴇᴄᴛɪᴏɴ.
2. sᴇɴᴅ <code>/connect</code> ғᴏʀ ᴄᴏɴɴᴇᴄᴛɪɴɢ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴘᴍ.

<b>ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ᴜsᴀɢᴇ:</b>
• <code>/connect</code>  - <code>ᴄᴏɴɴᴇᴄᴛ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴄʜᴀᴛ ᴛᴏ ʏᴏᴜʀ ᴘᴍ.</code>
• <code>/disconnect</code>  - <code>ᴅɪsᴄᴏɴɴᴇᴄᴛ ғʀᴏᴍ ᴀ ᴄʜᴀᴛ.</code>
• <code>/connections</code> - <code>ʟɪsᴛ ᴀʟʟ ʏᴏᴜʀ ᴄᴏɴɴᴇᴄᴛɪᴏɴs.</code>"""



# ---------------------» ᴇxᴛʀᴀ-ᴍᴏᴅ-ᴛᴇxᴛ «--------------------- #

    EXTRAMOD_TXT = """ʜᴇʟᴘ : <b>ᴇxᴛʀᴀ ᴍᴏᴅᴜʟᴇs</b>

<b>ɴᴏᴛᴇ:</b>
ᴛʜᴇsᴇ ᴀʀᴇ ᴛʜᴇ ᴇxᴛʀᴀ ғᴇᴀᴛᴜʀᴇs ᴏғ sᴇᴀʀᴄʜ ʙᴏᴛ.

<b>ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ᴜsᴀɢᴇ:</b>
• <code>/id</code> - <code>ɢᴇᴛ ɪᴅ ᴏғ ᴀ sᴘᴇᴄɪғɪᴇᴅ ᴜsᴇʀ.</code>
• <code>/info</code>  - <code>ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴀ ᴜsᴇʀ.</code>
• <code>/imdb</code>  - <code>ɢᴇᴛ ᴛʜᴇ ғɪʟᴍ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ғʀᴏᴍ ɪᴍᴅʙ sᴏᴜʀᴄᴇ.</code>
• <code>/search</code>  - <code>ɢᴇᴛ ᴛʜᴇ ғɪʟᴍ ɪɴғᴏᴍᴀᴛɪᴏɴ ғʀᴏᴍ ᴠᴀʀɪᴏᴜs sᴏᴜʀᴄᴇ.</code>
• <code>/speedtest</code> - <code>ɢᴇᴛ ᴛʜᴇ sᴘᴇᴇᴅ ᴏғ ʙᴏᴛ ᴡᴏʀᴋɪɴɢ ᴀɴᴅ ᴀʟsᴏ sᴇʀᴠᴇᴅ sᴘᴇᴇᴅ.</code> : desperate"""



# ---------------------» ᴀᴅᴍɪɴ-ᴛᴇxᴛ «--------------------- #

    ADMIN_TXT = """ʜᴇʟᴘ : <b>ᴀᴅᴍɪɴs ᴍᴏᴅs</b>

<b>NOTE:</b>
ᴛʜɪs ᴍᴏᴅᴜʟᴇ ᴏɴʟʏ ᴡᴏʀᴋs ғᴏʀ ᴍʏ ᴀᴅᴍɪɴs

<b>ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ᴜsᴀɢᴇ:</b>
• <code>/logs</code> - <code>ᴛᴏ ɢᴇᴛ ᴛʜᴇ ʀᴇsᴄᴇɴᴛ ᴇʀʀᴏʀs</code>
• <code>/stats</code> - <code>ᴛᴏ ɢᴇᴛ sᴛᴀᴛᴜs ᴏғ ᴏғ ғɪʟᴇs ɪɴ ᴅʙ.</code>
• <code>/delete</code> - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀ sᴘᴇᴄɪғɪᴄ ғɪʟᴇ ғʀᴏᴍ ᴅʙ.</code>
• <code>/users</code> - <code>ᴛᴏ ɢᴇᴛ ʟɪsᴛ ᴏғ ᴍʏ ᴜsᴇʀs ᴀɴᴅ ɪᴅs.</code>
• <code>/chats</code> - <code>ᴛᴏ ɢᴇᴛ ʟɪsᴛ ᴏғ ᴛʜᴇ ᴍʏ ᴄʜᴀᴛs ᴀɴᴅ ɪᴅs.</code>
• <code>/leave</code>  - <code>ᴛᴏ ʟᴇᴀᴠᴇ ғʀᴏᴍ ᴀ ᴄʜᴀᴛ.</code>
• <code>/disable</code>  -  <code>ᴅᴏ ᴅɪsᴀʙʟᴇ ᴀ ᴄʜᴀᴛ.</code>
• <code>/ban</code>  - <code>ᴛᴏ ʙᴀɴ ᴀ ᴜsᴇʀ.</code>
• <code>/unban</code>  - <code>ᴛᴏ ᴜɴʙᴀɴ ᴀ ᴜsᴇʀ.</code>
• <code>/channel</code> - <code>ᴛᴏ ɢᴇᴛ ʟɪsᴛ ᴏғ ᴛᴏᴛᴀʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴄʜᴀɴɴᴇʟs.</code>
• <code>/broadcast</code> - <code>ᴛᴏ ʙʀᴏᴀᴅᴄᴀsᴛ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ᴜsᴇʀs.</code>"""



# ---------------------» sᴛᴀᴛᴜs-ᴛᴇxᴛ «--------------------- #

    STATUS_TXT = """ᴛᴏᴛᴀʟ ғɪʟᴇs : <code>{}</code>
 ᴛᴏᴛᴀʟ ᴜsᴇʀs: <code>{}</code>
 ᴛᴏᴛᴀʟ ᴄʜᴀᴛs: <code>{}</code>
 ᴜsᴇᴅ sᴛᴏʀᴀɢᴇ: <code>{}</code> ᴍɪʙ
 ғʀᴇᴇ sᴛᴏʀᴀɢᴇ: <code>{}</code> ᴍɪʙ"""



# ---------------------» ʟᴏɢ_ɢ-ᴛᴇxᴛ «--------------------- #

    LOG_TEXT_G = """#ɴᴇᴡɢʀᴏᴜᴘ
    
<b>᚛› ɢʀᴏᴜᴘ ⪼ {}(<code>{}</code>)</b>
<b>᚛› ᴛᴏᴛᴀʟ ᴍᴇᴍʙᴇʀs ⪼ <code>{}</code></b>
<b>᚛› ᴀᴅᴅᴇᴅ ʙʏ ⪼ {}</b>
"""


# ---------------------» ʟᴏɢ_ᴘ-ᴛᴇxᴛ «--------------------- #

    LOG_TEXT_P = """#ɴᴇᴡᴜsᴇʀs 
    
<b>᚛› ᴜsᴇʀ ɪᴅ - <code>{}</code></b>
<b>᚛› ɴᴀᴍᴇ - {}</b>
"""

    ALRT_TXT = """ʜᴇʟʟᴏ {},
ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ʏᴏᴜʀ ᴍᴏᴠɪᴇ ʀᴇQᴜᴇꜱᴛ,
ʀᴇQᴜᴇꜱᴛ ʏᴏᴜʀ'ꜱ..."""

    OLD_ALRT_TXT = """ʜᴇʏ {},
ʏᴏᴜ ᴀʀᴇ ᴜꜱɪɴɢ ᴏɴᴇ ᴏꜰ ᴍʏ ᴏʟᴅ ᴍᴇꜱꜱᴀɢᴇꜱ, 
ᴘʟᴇᴀꜱᴇ ꜱᴇɴᴅ ᴛʜᴇ ʀᴇQᴜᴇꜱᴛ ᴀɢᴀɪɴ."""
