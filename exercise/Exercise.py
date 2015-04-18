#!/usr/bin/python

import os
import sys
import subprocess

class Exercise():
    def __init__(self, name, seed, plain, plainSolution, tex, texSolution):
        self.name = name
        self.seed = seed
        self.plain = plain
        self.plainSolution = plainSolution
        self.tex = tex
        self.texSolution = texSolution

    def setPlain(self, plain):
        self.plain = plain

    def setPlainSolution(plainSolution):
        self.plainSolution = plainSolution

    def setTex(self, tex):
        self.tex = tex

    def setTexSolution(self, texSolution):
        self.texSolution = texSolution

    def generatePDF(self, tex, solution=False):
        if solution:
            suffix = "-solution"
        else:
            suffix = ""
        template = open("../template/template.tex", "r").read()
        exerciseTex = template.replace("%%%CONTENT%%%", tex)
        exerciseTexFileName = "../tmp/%s-%s%s.tex" % (self.getName(), self.seed, suffix)
        exerciseTexFile = open(exerciseTexFileName, "w")
        exerciseTexFile.write(exerciseTex)
        exerciseTexFile.close()
        returnCode = subprocess.call("pdflatex -halt-on-error -output-directory ../tmp/ %s" % exerciseTexFileName, stdout=subprocess.PIPE, shell=True)
        return "../tmp/%s-%s%s.pdf" % (self.getName(), self.seed, suffix)

    def getPDF(self):
        return self.generatePDF(self.tex)

    def getPDFSolution(self):
        return self.generatePDF(self.texSolution, solution=True)

    def getPlain(self):
        return self.plain

    def getPlainSolution(self):
        return self.plainSolution

    def getName(self):
        return self.name

#seed = sys.argv[1]

#random.seed(seed)
#summand1 = random.randint(1, 9)
#summand2 = random.randint(1, 9)
#name = "Summe"
#plain = "%i + %i = ?" % (summand1, summand2)
#tex = "$ %s $" % plain
#plainSolution = "%i + %i = %i" % (summand1, summand2, summand1 + summand2)
#texSolution = "$ %s $" % plainSolution

#exercise = Exercise(name, seed, plain, plainSolution, tex, texSolution)
#print exercise.getPDF()
#print exercise.getPDFSolution()
