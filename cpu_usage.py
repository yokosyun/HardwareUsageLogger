import os
import psutil
import time
import logging
import argparse


def get_argparse():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--save_dir",
        type=str,
        default="logs",
    )
    parser.add_argument(
        "--minutes",
        type=int,
        default=60,
    )
    parser.add_argument(
        "--sleep_time",
        type=int,
        default=2,
    )
    return parser.parse_args()


def main():
    args = get_argparse()
    os.makedirs(args.save_dir, exist_ok=True)

    sample_per_min = 60 / args.sleep_time
    iterations = int(args.minutes * sample_per_min)

    logging.basicConfig(
        filename=os.path.join(args.save_dir, "cpu_usage.log"),
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

    for i in range(iterations):
        logging.info(psutil.cpu_percent(percpu=True))
        time.sleep(args.sleep_time)


if __name__ == "__main__":
    main()
