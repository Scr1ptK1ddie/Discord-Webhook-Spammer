import subprocess
subprocess.check_call(['pip', 'install', 'discord_webhook', 'termcolor'])
import termcolor
from discord_webhook import DiscordWebhook
import time
import os

logo = '''
 __          __  _     _                 _       _____                                           
 \ \        / / | |   | |               | |     / ____|                                          
  \ \  /\  / /__| |__ | |__   ___   ___ | | __ | (___  _ __   __ _ _ __ ___  _ __ ___   ___ _ __ 
   \ \/  \/ / _ \ '_ \| '_ \ / _ \ / _ \| |/ /  \___ \| '_ \ / _` | '_ ` _ \| '_ ` _ \ / _ \ '__|
    \  /\  /  __/ |_) | | | | (_) | (_) |   <   ____) | |_) | (_| | | | | | | | | | | |  __/ |   
     \/  \/ \___|_.__/|_| |_|\___/ \___/|_|\_\ |_____/| .__/ \__,_|_| |_| |_|_| |_| |_|\___|_|   
                                                      | |                                        
    By: Scr1ptK1ddie                                  |_|                                        
    '''

def send_message(webhook_url, message, times, avatar_url=None):
    try:
        webhook = DiscordWebhook(url=webhook_url, content=message, avatar_url=avatar_url, username="Scr1iptK1ddie")
        for _ in range(times):
            response = webhook.execute()
            print(termcolor.colored(f'[+] {message} Successfuly sent!', 'green'))
    except Exception as e:
        print(termcolor.colored(f'[-] Error: {e}', 'red'))

def main():
    os.system("clear")
    print(termcolor.colored(logo,  "yellow"))
    webhook_url = input(termcolor.colored("[?] Enter the webhook URL: ", 'yellow'))
    avatar_url = "https://raw.githubusercontent.com/Scr1ptK1ddie/Discord-Webhook-Spammer/main/SK.png"
    message = input(termcolor.colored("[?] Enter the message: ", 'yellow'))
    times = int(input(termcolor.colored("[?] Enter the number of times: ", 'yellow')))
    os.system("clear")

    send_message(webhook_url, message, times, avatar_url)

if __name__ == "__main__":
    main()
