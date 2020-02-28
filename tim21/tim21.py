import argparse
import os
from dotenv import load_dotenv
load_dotenv()


def usage():
    parser = argparse.ArgumentParser(description="Algorithmic trading bot")
    parser.add_argument('--config', dest="config",
                        type=str, help="config path")
    parser.add_argument('--mode', dest="mode", default="demo",
                        type=str, help="demo | real")
    args = parser.parse_args()
    return args


def boot_tim21():
    args = usage()
    print(f"Tim21 booted with mode: {args.mode}")


if __name__ == "__main__":
    boot_tim21()
