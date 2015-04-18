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

b = random.randint(5, 20)
c = random.randint(5, 20)
d = random.randint(2, 6)
e = d * random.randint(2, 8)
a = e / d
while a == e / d:
    a = random.randint(2, 9)

name = "log-Gleichung"
plain = "ln(sqrt(%i^(%i-x))) + %i*ln(%i) = %i*ln(%i)" % (a, b, c, d, c, e)
tex = r"ln{\sqrt{%i^{%i-x}}} + %i \cdot ln{%i} = %i \cdot ln{%i}" % (a, b, c, d, c, e)
plainSolution = ""
texSolution = r"\begin{IEEEeqnarray*}{rCll} \\ " +\
              r" \ln{\sqrt{%i^{%i-x}}} + %i \cdot \ln{%i} & = & %i \cdot \ln{%i} & \big| - %i \cdot \ln{%i} \\" % (a, b, c, d, c, e, c, d) +\
              r" \ln{\sqrt{%i^{%i - x}}} & = & %i \cdot \ln{%i} - %i \cdot \ln{%i} \\" % (a, b, c, e, c, d) +\
              r" \ln{\sqrt{%i^{%i - x}}} & = & \ln{%i^{%i}} - \ln{%i^{%i}} \\" % (a, b, e, c, d, c) +\
              r" \ln{\sqrt{%i^{%i - x}}} & = & \ln{\frac{%i}{%i}^{%i}} & \big| e^{( )} \\" % (a, b, e, d, c) +\
              r" \sqrt{%i^{%i - x}} & = & {%i}^{%i} & \big| {( )}^{2} \\" % (a, b, e / d, c) +\
              r" %i^{%i - x} & = & {%i}^{%i} & \big| \log_{%i} \\" % (a, b, e / d, 2 * c, a) +\
              r" %i - x & = & \log_{%i}{{%i}^{%i}} & \big| -%i \ \ \big| \cdot (-1) \\" % (b, a, e / d, 2 * c, b) +\
              r" x & = & %i - \log_{%i}{{%i}^{%i}} & \\" % (b, a, e / d, 2 * c) +\
              r" x & = & %i - %i \cdot \frac{\ln{%i}}{\ln{%i}} & " % (b, 2 * c, e / d, a)

texSolution +=  " \end{IEEEeqnarray*}"
tex = "$ %s $" % tex

exercise = Exercise.Exercise(name, seed, plain, plainSolution, tex, texSolution)
if args.plain:
    print exercise.getPlain()
    print exercise.getPlainSolution()
elif args.pdf:
    print exercise.getPDF()
    print exercise.getPDFSolution()
else:
    sys.exit(1)
