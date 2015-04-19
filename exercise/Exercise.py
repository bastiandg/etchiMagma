#!/usr/bin/python3

import os
import sys
import subprocess
import numpy
import matplotlib.pyplot as plot
from matplotlib.backends.backend_pdf import PdfPages

class Exercise():
    def __init__(self, name, seed, plain, plainSolution, tex, texSolution):
        self.name = name
        self.seed = seed
        self.plain = plain
        self.plainSolution = plainSolution
        self.tex = tex
        self.texSolution = texSolution
        self.graphicCount = 0

    def setPlain(self, plain):
        self.plain = plain

    def setPlainSolution(self, plainSolution):
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
        returnCode = subprocess.call("pdflatex -halt-on-error -output-directory ../tmp/ '%s'" % exerciseTexFileName, stdout=subprocess.PIPE, shell=True)
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

    def plotFunction(self, x = None, y = None, pointList = None, minX = 5, maxX = 5, minY = 5, maxY = 5):
        self.graphicCount += 1
        exerciseGraphicFile = "../tmp/%s-%s-%i.pdf" % (self.getName(), self.seed, self.graphicCount)
        with PdfPages(exerciseGraphicFile) as pdf:
            figure = plot.figure(figsize = (10, 10))
            ax = figure.add_subplot(111, aspect = "equal")
            ax.xaxis.set_ticks([i for i in range(-10, 10)])
            ax.yaxis.set_ticks([i for i in range(-10, 10)])

            ax.spines['left'].set_position('zero')
            ax.spines['right'].set_color('none')
            ax.spines['bottom'].set_position('zero')
            ax.spines['top'].set_color('none')

            ax.grid(True)
            plot.axis([-5, 5, -5, 5])
            if x != None and y != None:
                plot.plot(x, y)
            if pointList:
                plot.plot(*zip(*pointList), marker='o', color='r', ls='')
            pdf.savefig()
            plot.close()
        return exerciseGraphicFile

