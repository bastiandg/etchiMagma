#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
import random
import numpy as np
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
name = "LineareGleichung"

x1 = random.randint(-5, 5)
x2 = x1
while x1 == x2:
    x2 = random.randint(-5, 5)
if x1 > x2:
    tmp = x1
    x1 = x2
    x2 = tmp

y1 = random.randint(-5, 5)
y2 = y1
while y1 == y2:
    y2 = random.randint(-5, 5)
#if y1 > y2:
    #tmp = y1
    #y1 = y2
    #y2 = tmp

plain = u"Welche lineare Funktion verläuft durch die Punkte (%i, %i) und (%i, %i)?" % (x1, y1, x2, y2)
exercise = Exercise.Exercise(name, seed, plain, "", "", "")
x = np.arange(-5, 5.1, 0.1)
m = float(float(y1 - y2)/ float(x1 - x2))
b = float(y1) - float(float(y1 - y2)/float(x1 - x2)) * float(x1)
y = m * x + b

exerciseGraphic = exercise.plotFunction(pointList = [[x1, y1], [x2, y2]])
solutionGraphic = exercise.plotFunction(x = x, y = y, pointList = [[x1, y1], [x2, y2]])
tex = "%s \\\\ \includegraphics[width=12cm,height=12cm]{%s}" % (plain, exerciseGraphic)
exercise.setTex(tex)
plainSolution = "f(x) = %.2f * x + %.2f" % (m, b)
exercise.setPlainSolution(plainSolution)
if m == int(m):
    mTex = "%i" % int(m)
else:
    g = gcd((y1 - y2), (x1 - x2))
    if ((y1 - y2) < 0 and (x1 - x2) > 0) or ((y1 - y2) > 0 and (x1 - x2) < 0):
        mTex = r"- \frac{%i}{%i}" % (- (y1 - y2) / g, (x1 - x2) / g)
    else:
        mTex = r"\frac{%i}{%i}" % ((y1 - y2) / g, (x1 - x2) / g)

if b == int(b):
    bTex = "%i" % int(b)
else:
    g = gcd(y1 * (x1 - x2) - x1 * (y1 - y2), (x1 - x2))
    if (y1 * (x1 - x2) - x1 * (y1 - y2) < 0 and (x1 - x2) > 0) or (y1 * (x1 - x2) - x1 * (y1 - y2) > 0 and (x1 - x2) < 0):
        bTex = r"- \frac{%i}{%i}" % (- (y1 * (x1 - x2) - x1 * (y1 - y2)) / g, (x1 - x2) / g)
    else:
        bTex = r"\frac{%i}{%i}" % ((y1 * (x1 - x2) - x1 * (y1 - y2)) / g, (x1 - x2) / g)

texSolution = r"%s \\" % plain +\
              r"\begin{IEEEeqnarray*}{rCll} \\ " +\
              r"y_2 & = & m \cdot x_1 + b & \\" +\
              r"y_2 & = & m \cdot x_2 + b & \\" +\
              r"y_1 - y_2 & = & m (x_1 - x_2) & \big| : (x_1 - x_2) \\" +\
              r"m & = & \frac{y_1 - y_2}{x_1 - x_2} & \\" +\
              r"m & = & \frac{%i - %i}{%i - %i} & \\" % (y1, y2, x1, x2) +\
              r"m & = & %s & \\  \\" % mTex +\
              r"y_1 & = & m \cdot x_1 + b & \big| - m \cdot x_1 \\" +\
              r"b & = & y_1 - m \cdot x_1 & \\ " +\
              r"b & = & %i - (%s \cdot %i) & \\" % (y1, mTex, x1) +\
              r"b & = & %s & \\ \\" % bTex
if b < 0:
    texSolution += r"f(x) & = & %s x %s & \\" % (mTex, bTex)
elif b == 0:
    texSolution += r"f(x) & = & %s x & \\" % mTex
else:
    texSolution += r"f(x) & = & %s x + %s & \\" % (mTex, bTex)
texSolution += " \end{IEEEeqnarray*} \\\\"
texSolution += "\includegraphics[width=12cm,height=12cm]{%s}" % solutionGraphic
exercise.setTexSolution(texSolution)


if args.plain:
    print(exercise.getPlain())
    print(exercise.getPlainSolution())
elif args.pdf:
    print(exercise.getPDF())
    print(exercise.getPDFSolution())
else:
    sys.exit(1)
