import argparse
import os

from docx import Document

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help="Input path file")
parser.add_argument("-o", "--output", help="Output path file")
parser.add_argument("-f", "--font", help="Font name", default="Arial")

args = parser.parse_args()

inputFile = args.input
outputFile = args.output
fontName = args.font

document = Document(inputFile)

for paragraph in document.paragraphs:
    for run in paragraph.runs:
        run.font.name = fontName

if not outputFile:
	basename = os.path.basename(inputFile)
	dirname = os.path.dirname(inputFile)
	if not dirname:
		outputFile = "result_"+basename
	else:
		outputFile = dirname+"/result_"+basename

document.save(outputFile)
print("Result: " + outputFile)
