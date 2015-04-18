#!/usr/bin/python

import os
import sys
import random
import Exercise
os.chdir(os.path.dirname(os.path.realpath(sys.argv[0])))
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--seed", help="Seed for the exercise")
parser.add_argument("--plain", action="store_true", help="Print the exercise and solution in plain text")
parser.add_argument("--pdf", action="store_true", help="Generate PDF files for the exercise and the solution")

args = parser.parse_args()

if args.seed:
    seed = args.seed
else:
    seed = str(random.random())

random.seed(seed)

summand1 = random.randint(1, 9)
summand2 = random.randint(1, 9)
name = "Summe"
plain = "%i + %i = ?" % (summand1, summand2)
tex = "$ %s $" % plain
plainSolution = "%i + %i = %i" % (summand1, summand2, summand1 + summand2)
texSolution = "$ %s $" % plainSolution

exercise = Exercise.Exercise(name, seed, plain, plainSolution, tex, texSolution)
if args.plain:
    print exercise.getPlain()
    print exercise.getPlainSolution()
elif args.pdf:
    print exercise.getPDF()
    print exercise.getPDFSolution()
else:
    sys.exit(1)
