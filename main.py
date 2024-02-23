import subprocess
subprocess.check_call(['pip', 'install', 'discord_webhook', 'termcolor'])
import termcolor
from discord_webhook import DiscordWebhook
import time

def send_message(webhook_url, message, times, avatar_url=None):
    try:
        webhook = DiscordWebhook(url=webhook_url, content=message, avatar_url=avatar_url, username="Scr1iptK1ddie")
        for _ in range(times):
            response = webhook.execute()
            print(termcolor.colored(f'[+] {message} Successfuly sent!', 'green'))
    except Exception as e:
        print(termcolor.colored(f'[-] Error: {e}', 'red'))

def main():
    webhook_url = input(termcolor.colored("[?] Enter the webhook URL: ", 'yellow'))
    avatar_url = "https://raw.githubusercontent.com/Scr1ptK1ddie/Discord-Webhook-Spammer/main/SK.png"
    message = input(termcolor.colored("[?] Enter the message: ", 'yellow'))
    times = int(input(termcolor.colored("[?] Enter the number of times: ", 'yellow')))

    send_message(webhook_url, message, times, avatar_url)

if __name__ == "__main__":
    main()
