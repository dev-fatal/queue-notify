# QueueNotify (program)
## Description
Program that sends you a text when your Solo Shuffle pops in World of Warcraft. Developed for Windows 11 (but 10 should work).

**Please note that this program is in Alpha, and so you can expect errors to occur and things to be more difficult to set up for now. I've decided to release it despite the somewhat primitive state, as I think it will be useful for a lot of people who are able to follow the instructions below.**

Report any problems in the [Issues](https://github.com/dev-fatal/queue-notify/issues) tab, but please try searching things yourself first.

## Installation
1. Install the QueueNotify addon via [CurseForge](https://www.curseforge.com/wow/addons/queuenotify) or [Wago](https://addons.wago.io/addons/queuenotify) and then `/reload`
2. Install [Python 3 for Windows](https://www.python.org/downloads/) and ensure it's in your PATH. Note that this program has been tested on Python version 3.10
3. Download this repo (`git clone https://github.com/dev-fatal/queue-notify`, or [download the ZIP](https://github.com/dev-fatal/queue-notify/archive/refs/heads/main.zip) and then extract it somewhere)
4. Open Command Prompt and `cd` into where you saved it, e.g., `cd C:\Users\test\Documents\queue-notify`
5. Run `pip install -r requirements.txt` and wait until complete.


## Setup
1. Install the [Telegram app](https://telegram.org/apps) on your phone and sign up
2. Open a new message to the user `@BotFather` and type `/newbot`. You will then be prompted to fill in some values
3. Enter a name such as `QueueNotify`
4. Enter some unique username like `queuenotify_123456_bot`
5. Write down the HTTP API token you get, and enter it under `token` in the `config.toml` file
6. Ensure the `path` to your WoW folder in `config.toml` is correct. You must use double backslashes, e.g., `"C:\\Program Files (x86)\\World of Warcraft"`
7. Run the program (from inside the directory, as before) with `python main.py`. You will need to run this whenever you want to begin monitoring after a restart
8. When running for the first time, it will prompt you to send a message to your bot. Do this by clicking the `t.me/{username}` link given to you by the BotFather
9. Stop monitoring by closing the Command Prompt window.


## Updates
It is likely that this program will change significantly, and so you should check back here for updates. Please also keep the addon updated.


## Changing account
If you wish to change your linked Telegram account, simply change the `chat_id` value in `config.toml` to `""` and re-run the program.
