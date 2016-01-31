import os
import shutil
import zipfile

def packagePDF(assignment):
    students = os.listdir("{}/{}".format(os.getcwd(), assignment))
    new_dir = "inprog_{}".format(assignment)

    for student in students:
        if student == "grades.csv":
            continue

        # if no submission was entered, no submission will be returned
        if len(os.listdir("{}/{}/Submission attachment(s)".format(assignment, student))) == 0:
            continue

        uniqname = student[student.find("(")+1:student.find(")")]

        new_filename = "{}_{}.pdf".format(uniqname, assignment)
        shutil.copy("{}/{}_{}_feedback.pdf".format(new_dir, student, assignment), "{}/{}/Feedback attachment(s)/{}".format(assignment, student, new_filename))

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

    print("archive {}.zip created".format(assignment))
