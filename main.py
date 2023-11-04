### Dice roller decision maker

import random
import argparse

def dice(Dmin=1, Dmax=6):
   roll = random.randint(Dmin, Dmax)
   return roll


## Dice sized according to user-specified choices
def decision(choices):
    Dmax = len(choices)
    return dice(Dmax=Dmax)


def main():
    # get arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--choices", nargs="+", default=None, help="Comma-separated list of choices to choose from")
    args = parser.parse_args()
    
    if args.choices:
        # Roll dice, return the chosen choice
        # We subtract 1 from decision because args.choices starts at 0
        chosen = args.choices[decision(args.choices) - 1]
        print(f"chosen choice is {chosen}")
    else:
        parser.print_help()

if __name__ == "__main__":
   main()
