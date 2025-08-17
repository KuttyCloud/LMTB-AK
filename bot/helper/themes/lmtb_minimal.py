#!/usr/bin/env python3
class LMTBStyle:
    # ----------------------
    # async def start(client, message) ---> __main__.py
    ST_BN1_NAME = '𝐋ᴇᴇᴄʜ 𝐆ʀᴏᴜᴘ'
    ST_BN1_URL = 'https://t.me/EliteLeechZone'
    ST_BN2_NAME = '𝐔ᴘᴅᴀᴛᴇꜱ'
    ST_BN2_URL = 'https://t.me/HeartXBots'
    ST_MSG = '''<i>Now, Bot will send you all your files and links here. Start Using Now....</i>'''
    ST_BOTPM = '''<i>Now, This bot will send all your files and links here. Start Using ...</i>'''
    ST_UNAUTH = '''<i>You Are not authorized user! Deploy your own WZML-X Mirror-Leech bot</i>'''
    OWN_TOKEN_GENERATE = '''<b>Temporary Token is not yours!</b>\n\n<i>Kindly generate your own.</i>'''
    USED_TOKEN = '''<b>Temporary Token already used!</b>\n\n<i>Kindly generate a new one.</i>'''
    LOGGED_PASSWORD = '''<b>Bot Already Logged In via Password</b>\n\n<i>No Need to Accept Temp Tokens.</i>'''
    ACTIVATE_BUTTON = 'Activate Temporary Token'
    TOKEN_MSG = '''<b><u>Generated Temporary Login Token!</u></b>
<b>Temp Token:</b> <code>{token}</code>
<b>Validity:</b> {validity}'''
    # ---------------------
    # async def token_callback(_, query): ---> __main__.py
    ACTIVATED = '✅️ Activated ✅'
    # ---------------------
    # async def login(_, message): --> __main__.py
    LOGGED_IN = '<b>Already Bot Login In!</b>'
    INVALID_PASS = '<b>Invalid Password!</b>\n\nKindly put the correct Password .'
    PASS_LOGGED = '<b>Bot Permanent Login Successfully!</b>'
    LOGIN_USED = '<b>Bot Login Usage :</b>\n\n<code>/cmd [password]</code>'
    # ---------------------
    # async def log(_, message): ---> __main__.py
    LOG_DISPLAY_BT = '📑 Log Display'
    WEB_PASTE_BT = '📨 Web Paste (SB)'
    # ---------------------
    # async def bot_help(client, message): ---> __main__.py
    BASIC_BT = 'Basic'
    USER_BT = 'Users'
    MICS_BT = 'Mics'
    O_S_BT = 'Owner & Sudos'
    CLOSE_BT = 'Close'
    HELP_HEADER = "㊂ <b><i>Help Guide Menu!</i></b>\n\n<b>NOTE: <i>Click on any CMD to see more minor detalis.</i></b>"

    # async def stats(client, message):
    BOT_STATS = '''🤖 <b>BOT STATISTICS 🤖</b>

<b>⏰ Bot Uptime :</b> <code>{bot_uptime}</code>

<b>🎮 RAM ( MEMORY ) 🎮</b>

<b>┌ {ram_bar} {ram}%</b>
<b>├ Used:</b> <code>{ram_u}</code>
<b>├ Free :</b> <code>{ram_f}</code>
<b>└ Total :</b> <code>{ram_t}</code>

<b>💿 SWAP MEMORY 💿</b>

<b>┌ {swap_bar} {swap}%</b>
<b>├ Used:</b> <code>{swap_u}</code>
<b>├ Free :</b> <code>{swap_f}</code>
<b>└ Total :</b> <code>{swap_t}</code>

<b>💾 DISK 💾</b>

<b>┌ {disk_bar} {disk}%</b>
<b>├ Total Disk Read :</b> <code>{disk_read}</code>
<b>├ Total Disk Write :</b> <code>{disk_write}</code>
<b>├ Used :</b> <code>{disk_u}</code>
<b>├ Free :</b> <code>{disk_f}</code>
<b>└ Total :</b> <code>{disk_t}</code> 
    '''
    
    SYS_STATS = '''<b>📊 OS SYSTEM 📊</b>
    
<b>🟢 OS Uptime :</b> <code>{os_uptime}</code>

<b>🤖 OS Version :</b> <code>{os_version}</code>

<b>🛠 OS Arch :</b> <code>{os_arch}</code>

<b>📶 NETWORK STATS 📶</b>

<b>┌ Upload Data:</b> {up_data}
<b>├ Download Data:</b> {dl_data}
<b>├ Pkts Sent:</b> {pkt_sent}k
<b>├ Pkts Received:</b> {pkt_recv}k
<b>└ Total I/O Data:</b> {tl_data}

<b>🖥️ CPU 🖥️</b>

<b>┌ {cpu_bar} {cpu}%</b>
<b>├ CPU Frequency :</b> <code>{cpu_freq}</code>
<b>├ System Avg Load :</b> <code>{sys_load}</code>
<b>├ P-Core(s) :</b> <code>{p_core}</code>
<b>├ V-Core(s) :</b> <code>{v_core}</code>
<b>├ Total Core(s) :</b> <code>{total_core}</code>
<b>└ Usable CPU(s) :</b> <code>{cpu_use}</code>
    '''
    
    REPO_STATS = '''<b>🧑‍💻 REPO STATISTICS 🧑‍💻</b>
    
<b>┌ Bot Updated :</b> <code>{last_commit}</code>
<b>├ Current Version :</b> <code>{bot_version}</code>
<b>├ Latest Version :</b> <code>{lat_version}</code>
<b>├ Last ChangeLog :</b> <code>{commit_details}</code>
<b>└ REMARKS :</b> <code>{remarks}</code>
    '''
    
    BOT_LIMITS = '''<b>🚨 BOT LIMITATIONS 🚨</b>
    
<b>┌ Direct Limit :</b> <code>{DL} GB</code>
<b>├ Torrent Limit :</b> <code>{TL} GB</code>
<b>├ GDrive Limit :</b> <code>{GL} GB</code>
<b>├ YT-DLP Limit :</b> <code>{YL} GB</code>
<b>├ Playlist Limit :</b> <code>{PL} GB</code>
<b>├ Mega Limit :</b> <code>{ML} GB</code>
<b>├ Clone Limit :</b> <code>{CL} GB</code>
<b>└ Leech Limit :</b> <code>{LL} GB</code>

<b>┌ Token Validity :</b> <code>{TV}</code>
<b>├ User Time Limit :</b> <code>{UTI} / task</code>
<b>├ User Parallel Tasks :</b> <code>{UT}</code>
<b>└ Bot Parallel Tasks :</b> <code>{BT}</code>
    '''
    # ---------------------

    # async def restart(client, message): ---> __main__.py
    RESTARTING = '<i>Restarting...</i>'
    # ---------------------

    # async def restart_notification(): ---> __main__.py
    RESTART_SUCCESS = '''<b>Restarted Successfully!</b>

<b>┌ Date:</b> {date}
<b>├ Time:</b> {time}
<b>├ TimeZone:</b> {timz}
<b>└ Version:</b> {version}'''
    
    RESTARTED = '''<b>Bot Restarted !!!</b>'''
    # ---------------------

    # async def ping(client, message): ---> __main__.py
    PING = '<i>Starting Ping..</i>'
    PING_VALUE = '<b>Pong</b>\n<code>{value} ms..</code>'
    # ---------------------

    # async def onDownloadStart(self): --> tasks_listener.py
    LINKS_START = """
<b>Task Started</b>

<b>Mode:</b> {Mode}

<b>By:</b> {Tag}\n\n"""
    LINKS_SOURCE = """
<u><b>Source</b></u>

<b>Added On :</b> {On}

<b>▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬</b>

{Source}

<b>▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬</b>\n\n"""
    
    # async def __msg_to_reply(self): ---> pyrogramEngine.py
    PM_START =            "<b><u>Task Started :</u></b>\n\n<b>Link:</b> <a href='{msg_link}'>Click Here</a>"
    L_LOG_START =           "<b><u>Leech Started :</u></b>\n\n<b>User :</b> {mention} ( #ID{uid} )\n<b>Source :</b> <a href='{msg_link}'>Click Here</a>"

    # async def onUploadComplete(): ---> tasks_listener.py
    NAME =                  '<code>{Name}</code>\n'
    SIZE =                  '<b>┌ Size: </b>{Size}\n'
    ELAPSE =                '<b>├ Elapsed: </b>{Time}\n'
    MODE =                  '<b>├ Mode: </b>{Mode}\n'

    # ----- LEECH -------
    L_TOTAL_FILES =         '<b>├ Total Files: </b>{Files}\n'
    L_CORRUPTED_FILES =     '<b>├ Corrupted Files: </b>{Corrupt}\n'
    L_CC =                  '<b>└ By: </b>{Tag}\n\n'
    PM_BOT_MSG =            '<b>File(s) have been Sent above</b>'
    L_BOT_MSG =             '<b>File(s) have been Sent to Bot PM (Private)</b>'
    L_LL_MSG =              '<b>File(s) have been Sent. Access via Links...</b>\n'
    
    # ----- MIRROR -------
    M_TYPE =                '<b>┌ Type: </b>{Mimetype}\n'
    M_SUBFOLD =             '<b>├ SubFolders: </b>{Folder}\n'
    TOTAL_FILES =           '<b>├ Files: </b>{Files}\n'
    RCPATH =                '<b>├ Path: </b><code>{RCpath}</code>\n'
    M_CC =                  '<b>└ By: </b>{Tag}\n\n'
    M_BOT_MSG =             '<b>Link(s) have been Sent to Bot PM (Private)</b>'
    # ----- BUTTONS -------
    CLOUD_LINK =      '☁️ Cloud Link'
    SAVE_MSG =        '📨 Save Message'
    RCLONE_LINK =     '♻️ RClone Link'
    DDL_LINK =        '📎 {Serv} Link'
    SOURCE_URL =      '🔐 Source Link'
    INDEX_LINK_F =    '🗂 Index Link'
    INDEX_LINK_D =    '⚡ Index Link'
    VIEW_LINK =       '🌐 View Link'
    CHECK_PM =        '📥 View in Bot PM'
    CHECK_LL =        '🖇 View in Links Log'
    MEDIAINFO_LINK =  '📃 MediaInfo'
    SCREENSHOTS =     '🖼 ScreenShots'
    # ---------------------

    # def get_readable_message(): ---> bot_utilis.py
    ####--------OVERALL MSG HEADER----------
    STATUS_NAME =       '<code>{Name}</code>'

    #####---------PROGRESSIVE STATUS-------
    BAR =            '\n<b>┌ </b> {Bar}'
    PROCESSED =      '\n<b>├ Processed:</b> {Processed}'
    STATUS =         '\n<b>├ Status:</b> <a href="{Url}">{Status}</a>'
    ETA =            '\n<b>├ ETA:</b> {Eta}'
    SPEED =          '\n<b>├ Speed:</b> {Speed}'
    ELAPSED =        '\n<b>├ Elapsed:</b> {Elapsed}'
    ENGINE =         '\n<b>├ Engine:</b> {Engine}'
    STA_MODE =       '\n<b>├ Mode:</b> {Mode}'
    SEEDERS =        '\n<b>├ Seeders:</b> {Seeders} | '
    LEECHERS =                                           '<b>Leechers:</b> {Leechers}'

    ####--------SEEDING----------
    SEED_SIZE =      '\n<b>├ Size: </b>{Size}'
    SEED_SPEED =     '\n<b>├ Speed: </b> {Speed} | '
    UPLOADED =       '\n<b>├ Uploaded: </b> {Upload}'
    RATIO =          '\n<b>├ Ratio: </b> {Ratio} | '
    TIME =           '\n<b>├ Time: </b> {Time}'
    SEED_ENGINE =    '\n<b>├ Engine:</b> {Engine}'

    ####--------NON-PROGRESSIVE + NON SEEDING----------
    STATUS_SIZE =    '\n<b>├ Size: </b>{Size}'
    NON_ENGINE =     '\n<b>├ Engine:</b> {Engine}'

    ####--------OVERALL MSG FOOTER----------
    USER =           '\n<b>├ User:</b> <code>{User}</code> | '
    ID =                                                        '<b>ID:</b> <code>{Id}</code>'
    BTSEL =          '\n<b>├ Select:</b> {Btsel}'
    CANCEL =         '\n<b>└ Cancel:</b> {Cancel}\n\n'

    ####------FOOTER--------
    FOOTER =         '⌬ <b><i>Bot Stats</i></b>\n'
    TASKS =          '\n<b>├Tasks:</b> {Tasks}\n'
    BOT_TASKS =      '\n<b>├ Tasks:</b> {Tasks}/{Ttask} | <b>AVL:</b> {Free}\n'
    Cpu =            '\n<b>├ CPU:</b> {cpu}% | '
    FREE =           '<b>F:</b> {free} [{free_p}%]'
    Ram =            '\n<b>├ RAM:</b> {ram}% | '
    uptime =         '<b>UPTIME:</b> {uptime}'
    DL =             '\n<b>└ DL:</b> {DL}/s | '
    UL =             '<b>UL:</b> {UL}/s'

    ###--------BUTTONS-------
    PREVIOUS = '<<'
    REFRESH = '{Page}'
    NEXT = '>>'
    REFRESHS = '♻️'
    INFO = '☰'
    CLOSE = '❎'
    # ---------------------

    #STOP_DUPLICATE_MSG: ---> clone.py, aria2_listener.py, task_manager.py
    STOP_DUPLICATE = 'File/Folder is already available in Drive.\nHere are {content} list results:'
    # ---------------------

    # async def countNode(_, message): ----> gd_count.py
    COUNT_MSG = '<b>Counting:</b> <code>{LINK}</code>'
    COUNT_NAME = '<b><i>{COUNT_NAME}</i></b>\n┃\n'
    COUNT_SIZE = '┠ <b>Size: </b>{COUNT_SIZE}\n'
    COUNT_TYPE = '┠ <b>Type: </b>{COUNT_TYPE}\n'
    COUNT_SUB =  '┠ <b>SubFolders: </b>{COUNT_SUB}\n'
    COUNT_FILE = '┠ <b>Files: </b>{COUNT_FILE}\n'
    COUNT_CC =   '┖ <b>By: </b>{COUNT_CC}\n'
    # ---------------------

    # LIST ---> gd_list.py
    LIST_SEARCHING = '<b>Searching for <i>{NAME}</i></b>'
    LIST_FOUND = '<b>Found {NO} result for <i>{NAME}</i></b>'
    LIST_NOT_FOUND = 'No result found for <i>{NAME}</i>'
    # ---------------------

    # async def mirror_status(_, message): ----> status.py
    NO_ACTIVE_DL = '''<b>No Active Downloads !!!</b>
    
<b>🤖 Bot Stats 🤖</b>

<b>┌ 🖥 CPU :</b> {cpu}%
<b>├ 💿 Free :</b> {free} [{free_p}%]
<b>├ 🎮 RAM :</b> {ram}
<b>├ 🟢 UPTIME :</b> {uptime}
<b>├ 🔻 DL :</b> {DLX}/s
<b>└ 🔺 UL :</b> {ULX}/s

<b>Don't trust anyone life is full of fake people</b>
    '''
    # ---------------------

    # USER Setting --> user_setting.py 
    USER_SETTING = '''㊂ <b><u>User Settings :</u></b>
        
┎<b> Name :</b> {NAME} ( <code>{ID}</code> )
┠<b> Username :</b> {USERNAME}
┠<b> Telegram DC :</b> {DC}
┖<b> Language :</b> {LANG}

➲ <u><b>Available Args:</b></u>
• <b>-s</b> or <b>-set</b>: Set Directly via Arg'''

    UNIVERSAL = '''㊂ <b><u>Universal Settings : {NAME}</u></b>

┎<b> YT-DLP Options :</b> <b><code>{YT}</code></b>
┠<b> Daily Tasks :</b> <code>{DT}</code> per day
┠<b> Last Bot Used :</b> <code>{LAST_USED}</code>
┠<b> User Session :</b> <code>{USESS}</code>
┠<b> MediaInfo Mode :</b> <code>{MEDIAINFO}</code>
┠<b> Save Mode :</b> <code>{SAVE_MODE}</code>
┖<b> User Bot PM :</b> <code>{BOT_PM}</code>'''

    MIRROR = '''㊂ <b><u>Mirror/Clone Settings : {NAME}</u></b>

┎<b> RClone Config :</b> <i>{RCLONE}</i>
┠<b> Mirror Prefix :</b> <code>{MPREFIX}</code>
┠<b> Mirror Suffix :</b> <code>{MSUFFIX}</code>
┠<b> Mirror Remname :</b> <code>{MREMNAME}</code>
┠<b> DDL Server(s) :</b> <i>{DDL_SERVER}</i>
┠<b> User TD Mode :</b> <i>{TMODE}</i>
┠<b> Total User TD(s) :</b> <i>{USERTD}</i>
┖<b> Daily Mirror :</b> <code>{DM}</code> per day'''

    LEECH = '''㊂ <b><u>Leech Settings for {NAME}</u></b>

┎<b> Daily Leech : </b><code>{DL}</code> per day
┠<b> Leech Type :</b> <i>{LTYPE}</i>
┠<b> Custom Thumbnail :</b> <i>{THUMB}</i>
┠<b> Leech Split Size :</b> <code>{SPLIT_SIZE}</code>
┠<b> Equal Splits :</b> <i>{EQUAL_SPLIT}</i>
┠<b> Media Group :</b> <i>{MEDIA_GROUP}</i>
┠<b> Leech Caption :</b> <code>{LCAPTION}</code>
┠<b> Leech Prefix :</b> <code>{LPREFIX}</code>
┠<b> Leech Suffix :</b> <code>{LSUFFIX}</code>
┠<b> Leech Dumps :</b> <code>{LDUMP}</code>
┠<b> Metadata :</b> <b><code>{METADATA}</code></b>
┠<b> Attachment :</b> <code>{ATTACHMENT}</code>
┖<b> Leech Remname :</b> <code>{LREMNAME}</code>'''
