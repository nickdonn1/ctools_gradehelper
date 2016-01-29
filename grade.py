from tempfile import NamedTemporaryFile
import shutil
import csv
import os
from subprocess import call

if __name__ == "__main__":
    EDITOR = os.environ.get("EDITOR", "vim")

    assignment = raw_input("Name of Assignment: ")
    os.chdir(assignment)

    while True:
        rawin = raw_input("grader>> ")
        cmd, uniqname = rawin.split()

        if (cmd == "g" or cmd == "grade"):
            tempfile = NamedTemporaryFile(delete=False)
            grade = raw_input("Enter grade: ")

            with open("grades.csv".format(assignment)) as csvFile, tempfile:
                reader = csv.reader(csvFile, delimiter=',', quotechar='"')
                writer = csv.writer(tempfile, delimiter=',', quotechar='"')

                for row in reader:
                    if len(row) == 0:
                        continue
                    if row[0] == uniqname:
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
                    call([EDITOR, "{}/comments.txt".format(student)])

        else:
            exit()