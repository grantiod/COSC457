This is the term project.

This file is called a README. It acts as a frontpage for this repository with instructions and useful info.

To use the project locally, Git will be needed.
In Git, move to the directory you want to store the project and type "git clone https://github.com/grantiod/COSC457.git"
This will create a directory called COSC457. Move into this directory in Git.

dbui.py is the main file for the project.
Employee, Patient, etc. are classes that act as pop-up windows.
Each class name corresponds to a different table in the DB.

To use dbui.py, there must be a MySQL server run locally.
If you do not have one, open one on MySQL Workbench.
Whatever username and password you use to run your MySQL server locally must be used in substiution for the
username and password I have in each of the class files (all non-dbui.py files). You will need to go in and
edit the files individually so the UI can connect to the MySQL server.