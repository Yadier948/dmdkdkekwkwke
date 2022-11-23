import os
import ProxyCloud

BOT_TOKEN =  os.environ.get('bot_token','5325291385:AAHWftRu9ikAjwi7HBlXhW9VL2jk8vJcAYM')
API_ID =  os.environ.get('api_id','18641760')
API_HASH = os.environ.get('api_hash','b7b026ce9d1d36400c02dc21d8df53a3')
SPLIT_FILE = 1024 * 1024 * int(os.environ.get('split_file','99'))
ROOT_PATH = 'root/'
ACCES_USERS = os.environ.get('tl_admin_user','countryandlifee').split(';countryandlifee')
#ACCES_USERS = ('tl_admin_user','countryandlifee')
#ACCES_USERS = os.environ.get(countryandlifee)
PROXY = ProxyCloud.parse(os.environ.get('proxy_enc','http://KGGJJJYIJFLIFEYDJFLEKHYGCHDHRHHKCHHGCE'))

if PROXY:
  print(f'Proxy {PROXY.as_dict_proxy()}')
