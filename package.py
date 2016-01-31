import os
import shutil
import zipfile
import sys

def packagePDF(assignment):
    cwd = os.getcwd()
    students = os.listdir(os.path.join(cwd, "{}".format(assignment)))
    new_dir = "inprog_{}".format(assignment)

    for student in students:
        if student == "grades.csv":
            continue

        # if no submission was entered, no submission will be returned
        if len(os.listdir(os.path.join(cwd, "{}/{}/Submission attachment(s)".format(assignment, student)))) == 0:
            continue

        uniqname = student[student.find("(")+1:student.find(")")]

        new_filename = "{}_{}_feedback.pdf".format(uniqname, assignment)
        shutil.copy(os.path.join(cwd, "{}/{}_{}.pdf".format(new_dir, student, assignment)), os.path.join(cwd, "{}/{}/Feedback attachment(s)/{}".format(assignment, student, new_filename)))

# http://stackoverflow.com/questions/1855095/how-to-create-a-zip-archive-of-a-directory
def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))

if __name__ == "__main__":
    # Ask for name of directory
    if (len(sys.argv) < 2):
        assignment = raw_input("Name of Assignment: ")
    else:
        assignment = sys.argv[1]

    pdf = raw_input("Include PDF feedback? [y/n]: ")

    if (pdf == "yes" or pdf == "y"):
        packagePDF(assignment)

    #zip files
    zipf = zipfile.ZipFile('{}.zip'.format(assignment), 'w')
    zipdir('{}/'.format(assignment), zipf)
    zipf.close()

    shutil.rmtree("inprog_{}".format(assignment))

    print "archive {}.zip created".format(assignment)
