import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
profile = [i.split(":")[1][1:-1] for i in data if 'All user profile' in i ]

for i in profile :
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles', i, 'key=clear']).decode('utf-8').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if 'Key Content' in b]
    try :
        print('{:<30} and {:<}'.format(i, results[0]))
    except :
        print('{:<30} and {:<}', format(i, ''))