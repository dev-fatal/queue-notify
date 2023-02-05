from message import get_chat_id
from monitor import monitor
import toml


def load_config():
    config_path = "config.toml"
    with open(config_path) as file:
        config = toml.load(file)
    if config["chat_id"] == "":
        chat_id = None
        while not chat_id:
            input("Please send a message to the Telegram bot you created. Once done, wait 1 minute then press Enter.")
            chat_id = get_chat_id(config["token"])
        config["chat_id"] = chat_id
        with open(config_path, "w") as file:
            toml.dump(config, file)
    return config


def main():
    config = load_config()
    monitor(config["path"], config["token"], config["chat_id"])


if __name__ == "__main__":
    main()
