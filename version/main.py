import micropython_ota

# connect to network
do_connect()

ota_host = 'https://iot.isabetonline.com'
project_name = 'micropython'
filenames = ['boot.py', 'main.py']
user = 'isabeton'
passwd = '993399_aRiF' # it's best to place this credential is a secrets.py file

micropython_ota.ota_update(ota_host, project_name, filenames, user=user, passwd=passwd, use_version_prefix=True, hard_reset_device=True, soft_reset_device=False, timeout=5)
