import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-v', '--verbose', help='increased output', action='store_true')
parser.add_argument("square", help="display square of a number", type=int)
args = parser.parse_args()

print(__file__)
if args.verbose:
   print("The square of %d equals %d" % (args.square, args.square**2))
else:
   print(args.square**2)
