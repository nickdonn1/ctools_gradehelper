# ctools_gradehelper
A little tool to help people grade with [the soon to be defunct] CTools (Sakai)
Tested on OSX

# Features
### grade.py
Provides a command line interface for assigning grades to individual students and providing student feedback.

### unpack.py
Moves and renames all student submissions to folder in working directory called "inprog_assignmentName" for ease of grading.
All modifications made to these pdf documents will be returned to students as feedback by using package.py
Requires that all assignments are submitted as single pdf documents

### package.py
Zips up assignment for upload to CTools.
If "yes" or "y" is selected for "Include PDF feedback?" prompt, the pdfs created by unpack.py will be packaged as student feedback.

## Setup
1. Clone repo

2. Download zip of student submissions

You can do that by clicking the link as shown below from the Assignments->Grade screen. Check the box to download All.
![Image of Download Link](https://github.com/nickdonn1/ctools_gradehelper/images/ctools_download.png)

3. Unzip student submissions and put repo and assignment folder in the same directory as shown below and cd into directory
![Image of Folder](https://github.com/nickdonn1/ctools_gradehelper/images/folder_struct.png)

## Usage
### grade.py
#### Run:
    ```
    $ python repo_name/grade.py "assignment_name"
    $ python repo_name/grade.py assignment_name
    $ python repo_name/grade.py
    ```

#### Commands:
    ##### Add/Change student grade
    ```
    [assignment_name]grader>> g uniqname
    [assignment_name]grader>> grade uniqname
    ```
    which will prompt:
    ```
    Enter grade for uniqname: 
    ```

    ##### Make comment to student
    ```
    [assignment_name]grader>> c uniqname
    [assignment_name]grader>> comment uniqname
    ```
    which will launch Vim and allow you to modify student comments

    ##### Exit
    ```
    [assignment_name]grader>> exit
    ```

### unpack.py
#### Run:
    ```
    $ python repo_name/unpack.py
    ```

### package.py
#### Run:
    ```
    $ python repo_name/package.py
    ```

## Uploading to CTools
From the Assignments->Grade screen, click "Upload All" and check the following before uploading your .zip file from package.py
* Grade file
* Feedback comments
* Feedback attachment(s)
