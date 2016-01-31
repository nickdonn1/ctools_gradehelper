from tempfile import NamedTemporaryFile
import shutil
import csv
import os
from subprocess import call
import sys
try:
  import readline
except ImportError:
  import pyreadline as readline

def printerror():
    print 'grader: valid commands include "exit", "<uniqname> g[rade]" and "<uniqname> c[omment]"'

if __name__ == "__main__":
    EDITOR = os.environ.get("EDITOR", "vim")

    if (len(sys.argv) < 2):
        assignment = raw_input("Name of Assignment: ")
    else:
        assignment = sys.argv[1]
    
    os.chdir(os.path.join(os.getcwd(), assignment))

    query = "[{}]grader>> ".format(assignment)

    while True:
        rawin = raw_input(query)

        if (rawin == "exit"):
            exit()

        try:
            uniqname, cmd = rawin.split()
        except:
            printerror()
            continue

        if (cmd == "g" or cmd == "grade"):
            tempfile = NamedTemporaryFile(delete=False)

            with open("grades.csv".format(assignment)) as csvFile, tempfile:
                reader = csv.reader(csvFile, delimiter=',', quotechar='"')
                writer = csv.writer(tempfile, delimiter=',', quotechar='"')

                for row in reader:
                    if len(row) == 0:
                        continue
                    if row[0] == uniqname:
                        grade = raw_input("Enter grade for {},{} ({}): ".format(row[2], row[3], uniqname))
                        if grade == "":
                            print "grade for uniqname cleared"
                        if len(row) < 5:
                            row.append(grade)
                        else:
                            row[4] = grade

                    writer.writerow(row)

            shutil.move(tempfile.name, "grades.csv")

        elif (cmd == "c" or cmd == "comment"):
            students = os.listdir(os.getcwd())

            for student in students:
                if student[student.find("(")+1:student.find(")")] == uniqname:
                    call([EDITOR, os.path.join(os.getcwd(), "{}/comments.txt".format(student))])

        else:
            printerror()