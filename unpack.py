import os
import shutil

if __name__ == "__main__":
    # Ask for name of directory
    assignment = raw_input("Name of Assignment: ")

    #get student directory names
    students = os.listdir("{}/{}".format(os.getcwd(), assignment))
    new_dir = "inprog_{}".format(assignment)
    os.mkdir(new_dir)

    for student in students:
        if student == "grades.csv":
            continue

        files = os.listdir("{}/{}/Submission attachment(s)".format(assignment, student))

        if len(files) == 0:
            continue

        if files[0].endswith(".pdf"):
            new_filename = "{}_{}.pdf".format(student, assignment)
            shutil.copy("{}/{}/Submission attachment(s)/{}".format(assignment, student, files[0]), "{}/{}".format(new_dir, new_filename))
            #shutil.copy("{}/{}/Submission attachment(s)/{}".format(assignment, student, files[0]), "{}/Feedback attachment(s)/{}".format(student, new_filename))