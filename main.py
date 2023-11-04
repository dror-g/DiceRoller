### Dice roller decision maker

import random
import argparse

def dice(Dmin=1, Dmax=6):
   roll = random.randint(Dmin, Dmax)
   return roll


def decision(choices):
    Dmax = len(choices)
    return dice(Dmax=Dmax)


def main():
    # get cli arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--choices", nargs="+", default=None, help="Comma-separated list of choices to choose from")
    args = parser.parse_args()
    
    if args.choices:
        chosen = args.choices[decision(args.choices) - 1]
        print(f"chosen choice is {chosen}")
    else:
        parser.print_help()

if __name__ == "__main__":
   main()
