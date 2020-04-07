import argparse
import sys


def reverse_bin(number: int) -> int:
    return int(bin(number)[2:][::-1], 2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('number', type=int, help='Input int number for reverse.'
                                                 ' Range of number should be in 1<= N <= 1000000000;')

    args = parser.parse_args()
    if not 1 <= args.number <= 1000000000:
        print("Invalid range of number. Number should be in 1:1000000000")
        sys.exit(1)

    print(reverse_bin(args.number))
