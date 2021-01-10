# Day One Doc

### This semester we will be building an internet enabled device (IoT) called "The Fam Cam". It will be a motion detection device that, when triggered, will send a notification to a user's device. This device will be built on a single-board computer with code written in Python that is built on a Linux-based operating system. Since we prepared this course to accommodate all levels of students, we will start assuming the student has no knowledge of programming or  computers. Seeing as we are starting from scratch, we will teach the basics of hardware and computers, operating systems, networking with computers, and programming in Python. Our final project will use a Raspberry Pi for the computer, Raspbian as the Linux-based operating system, and Python for the software needed for the notification system. We look forward to embarking on this journey with you to learning hardware and computer science!

0. We use certain typings that allow us to convey information to the user.

- Text wrapped in backticks `` (they are generally found in the top left of a keyboard along with the tilda "~")
should be directly copied and pasted. For example, `mkdir programming` as shown below would be directly copied and
pasted into your terminal window.

- Text wrapped in square brackets [] are meant to be replaced with text specific to the user. That text will be
described in the brackets. For example, if you wanted to change directories using the "cd" command, you could
enter the following `cd [directory name]`. If that directory was named "py-files", your command would look like
this- `cd py-files`. As you can see, the brackets are removed when you are inserting your own text.

- Text wrapped in double quotes is a reference to some text, or an action that should be taken by the user. These
are typically self-explanatory.

## If you have already taken the first semester of the CSX curriculum, you can skip the following.

1. Download Python -> https://www.python.org/downloads/
        a. IMPORTANT: Check off the "Add to Path" box when installing

2. Create a Github Account -> github.com
        a. Download Git -> https://git-scm.com/downloads
  
3. Download VS Code -> https://code.visualstudio.com/download
        
4. Create a folder named "programming" in your computer's "Documents" directory.
  
5. Open a new window in VS Code. Click "Open Folder". Find your programming folder. Click it once then click "Open".
        a. To open a terminal in VS Code click "Shift + Ctrl + `"
        b. Enter the command `pwd` into your terminal then click enter. Your "working directory" should
           be in the "programming" folder, and the path response you get from the pwd command should end in "programming"
           (i.e. user/Documents/programming)
        c. Create a folder called "python-work" by entering the command `mkdir python-work`
        d. Download the following VS Code extensions- Python and TODO Highlight. You can find the extensions tab in VS
           Code by clicking "Shift + Ctrl + X" (windows) or "Shift + Command + X" (mac). Once there, search for those exact extensions and download the first result for each of them. Once you are done downloading those extensions, return back to the main "Explorer" page where you will be viewing your folders/files by clicking "Shift + Ctrl + E" (windows) or "Shift + Command + E" (mac).
        
6. Create a repository in Github -> https://help.github.com/en/enterprise/2.13/user/articles/creating-a-new-repository
        Then copy this set of commands into your terminal after creating repository:
          - `echo "# [INSERT REPOSITORY NAME]" >> README.md`
          - `git init`
          - `git add README.md`
          - `git commit -m "first commit"`
          - `git remote add origin [REPOSITORY URL]`
          - `git push -u origin master`
          
7. To check what your working directory is once again, enter `pwd` into your terminal

8. When you want to go up a level in your directory, enter `cd ..` into your terminal
    ex: if you are in "/Users/user/Documents/programming/python-work"
        Enter in the Terminal: `cd ..`
        your working directory will then be "/Users/username/Documents/programming"

9. When you want to chamge your working directory, enter `cd [directory name]`
        For example, if you are in "/Users/username/Documents/programming"
        Enter in the Terminal: `cd python-work` (If you begin to type the name of the desired directory,
                                                 you can hit the tab button and the directory should fill in)
        your working directory will then be "/Users/username/Documents/programming/python-work"
        
10. The steps to commit code to Github are:
        `git add .`
        `git commit -m "commit message`
        `git push`
        
11. To pull code from the master branch of a repository:
        `git pull origin master`
        
12. Next you should copy and paste the todos (file ends in "todo") into VS Code
        a. Go to -> https://github.com/projectinnovatenewark/student_repository/tree/master/todos
           to see the assignment files separated by week.
        b. Create a file in your "python-work" folder in VS Code:
           right click on "python-work" folder
           click "new file"
           name the new file "currentlesson.py" (.py tells VS Code that it is a pthon file)
        c. Copy the first lesson from week one in your new file and try to solve it. 
           To run your code, simply click on the green arrow at the top right of your VS Code window.
 
13. When you are finished with the lesson and complete the corresponding todo
          (todos are meant to test what you learned from the lesson)
        a. repeat step 12.b but instead name the file "currentlessontodo.py"
        b. try to complete the todo and then peer review

### EXTRA INFO:
We style all of this text with Markdown. It's pretty cool. If you want to learn more about how to style, and potentially contribute to these texts, check out this link: https://docs.github.com/en/free-pro-team@latest/github/writing-on-github/basic-writing-and-formatting-syntax
