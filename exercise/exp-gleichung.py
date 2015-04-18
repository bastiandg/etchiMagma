#!/usr/bin/python

import os
import sys
import random
import Exercise
os.chdir(os.path.dirname(os.path.realpath(sys.argv[0])))
import argparse
from fractions import gcd

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

exponent1 = random.randint(2, 9)
exponent2 = random.randint(2, 9)
exponent3 = random.randint(1, 4) * 2
exponent4 = random.randint(1, 4) * 2
name = "e-Gleichung"
plain = "exp(%ix) * (exp(x)) ^ %i = sqrt(exp(-%i)/exp(%ix))" % (exponent1, exponent2, exponent3, exponent4)
tex = r"$ e^{%ix} \cdot (e^{x}) ^ %i = \sqrt{\frac{e^{-%i}}{e^{%ix}}} $" % (exponent1, exponent2, exponent3, exponent4)
plainSolution = "%i/%i" % (exponent3 / 2, (exponent1 + exponent2 + exponent4 / 2))
texSolution = r"\begin{IEEEeqnarray*}{rCl's} \\ " +\
              r"e^{%ix} \cdot (e^{x}) ^ %i & = & \sqrt{\frac{e^{-%i}}{e^{%ix}}} & \\" % (exponent1, exponent2, exponent3, exponent4) +\
              r" e^{%ix} \cdot e^{%ix} & = & \frac{e^{-%i}}{e^{%ix}} & \\" % (exponent1, exponent2, exponent3 / 2, exponent4 / 2) +\
              r" e^{%ix} & = & e^{-%i - %ix} & \big| ln \\" % (exponent1 + exponent2, exponent3 / 2, exponent4 / 2) +\
              r" %ix & = & -%i - %ix & \big| +%ix \\" % (exponent1 + exponent2, exponent3 / 2, exponent4 / 2, exponent4 / 2) +\
              r" %ix & = & -%i & \big| :%i \\" % (exponent1 + exponent2 + exponent4 / 2, exponent3 / 2, exponent1 + exponent2 + exponent4 / 2) +\
              r" x & = & -\frac{%i}{%i} & \\ " % (exponent3 / 2, exponent1 + exponent2 + exponent4 / 2)
greatestCommonDivisor = gcd(exponent3 / 2, exponent1 + exponent2 + exponent4 / 2)
if  greatestCommonDivisor > 1:
    texSolution += r" x & = & -\frac{%i}{%i}" % (exponent3 / 2 / greatestCommonDivisor, (exponent1 + exponent2 + exponent4 / 2) / greatestCommonDivisor)

texSolution +=  " \end{IEEEeqnarray*}"

exercise = Exercise.Exercise(name, seed, plain, plainSolution, tex, texSolution)
if args.plain:
    print exercise.getPlain()
    print exercise.getPlainSolution()
elif args.pdf:
    print exercise.getPDF()
    print exercise.getPDFSolution()
else:
    sys.exit(1)
