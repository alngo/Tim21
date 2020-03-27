import argparse
from .tim21 import Tim21
from dotenv import load_dotenv
load_dotenv()


def usage():
    parser = argparse.ArgumentParser(description="Algorithmic trading bot")
    parser.add_argument('--config', dest="config",
                        type=str, help="config path")
    args = parser.parse_args()
    return args


def boot_tim21():
    args = usage()
    config_path = "config.cfg" if args.config is not None else args.config
    bot = Tim21(config_path)
    print(f"Tim21 booted with config: {config_path}")
    bot.run()


if __name__ == "__main__":
    boot_tim21()
