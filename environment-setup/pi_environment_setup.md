<div align=center><h1>Evironment Setup</h1></div>

The purpose of this section is to introduce you to the following concepts: 
- Version Control
- Visual Studio Code
- Git
- GitHub
- Bash and Aliases

<div align=center><h3>Section 1: Visual Studio Code</h3></div>

In computing, **source code** is any collection of code that is written using a human-readable programming language, usually as plain text.

**Visual Studio (VS) Code** is a free source-code editor made by Microsoft for Windows, Linux and macOS. A **source-code editor** is a text editor program that is specialized for writing software.  

**insert image**

**Extensions** are add-ons that allow you to customize and enhance your experience in Visual Studio by adding new features or integrating existing tools. An extension can range in all levels of complexity, but its main purpose is to increase your productivity and cater to your workflow.

**INsert Image**

<h4>Installing Extensions</h4>
Use the following links to install the Visual Studio Code extensions we will be using in this course:

<ul>
<li>Python INSERT LINK</li>
<li>Highlight INSERT LINK</li>
</ul>

<div align=center><h3>Section 2: Version Control</h3></div>

**Version control** is a system that records changes to a file or set of files over time so that you can recall specific versions later.

In software development, a **repository** is a central file storage location. A **branch** is a version of a repository that can act as an independent line of development. A repository can contain multiple branches, which means there are multiple versions of the repository. 

<div align=center><h4>Git</h4></div>

**Git** is a distributed version-control system for tracking changes in source code during software development.

**INSERT GIT IMAGE**

**Basic Git Commands**
<ul>
    <li>
        <ins>Git Clone:</ins> primarily used to point to an existing repo and make a clone or copy of that repo at in a new directory, at another location
    </li>
    <li>
        <ins>Git Add:</ins> adds a change in a working directory to the staging area.
        <ul>
            <li>
                The <b>staging area</b> is like a rough draft space, it's where you can <b>git</b> add the version of a file or multiple files that you want to save in your next commit (in other words in the next version of your project).
            </li>
        </ul>
    </li>
    <li>
        <ins>Git Commit:</ins> used to save your changes to the local repository.
    </li>
    <li>
        <ins>Git Push:</ins> used to upload local repository content to a remote repository.
    </li>
    <li>
        <ins>Git Pull:</ins> used to fetch and download content from a remote repository and immediately update the local repository to match that content.
    </li>
    </ul>

<div align=center><h4>Github</h4></div>

**GitHub** is a code hosting platform for software development and version control using Git. It offers the distributed version control and source code management functionality of Git, plus its own features.

It is important to remember that Git and Github are not the same thing. 
- Git is a  tool used to manage your source code history. 
- GitHub is a hosting service for Git repositories.

In other words, Git is a version control tool and GitHub is the service for projects that use that tool.

**INSERT SCREENSHOT**

<div align=center><h3>Using GitHub, VS Code, and Git</h3></div>

<div ><h3>Creating the Programming Folder</h3></div>

**Insert screenshot of creating folder**

Open the Pi's file manager and then create  a folder called “programming” in the root directory.
> The file path will be "home/pi/"

This will be used as the main location in which you save everything coding related. Inside this folder, we are going to create a file, *hello_world.py*. Use `touch hello_world.py` to do so.

<a href="https://help.github.com/en/enterprise/2.13/user/articles/creating-a-new-repository">Click here to review GIthub’s documentation on creating a new repository.</a> Follow the steps in this walk through of how to create a new repository called “python-work”.
<br>
After completing the steps to create a repository, we must set up a local repository on your Pi to be used to update the remote repository.

1. First, change your working directory to your programming folder if it is not currently.
2. Use this <a href="https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-using-the-command-line">link</a> and follow the steps to learn how to clone repositories using the command line.
    - Use `git clone https://github.com/[YOUR USERNAME]/python-work` to clone the repository onto your local machine.
    - Doing so adds the directory to your current working directory.

<div ><h3>Adding Files to Local Repository</h3></div>

The “python-work” folder is where the student will be completing all of their coding assignments. Since creating folders and files was covered extensively, we will not be taking another deep dive. Instead, here is a list of options in doing so:

- touch
- echo
- cat
- Or the classic right-click (two-finger click on a Mac)

This is all done within your VS Code window either inside the Integrated Terminal or the file manager pop

<div ><h3>Updating Your Remote Repository</h3></div>
Updating the remote repository is best practice for a couple reasons:

- For starters, it is Git’s main function! If you don’t update the repository with the most recent changes to the code, then your team won’t have access to it to build cool apps.
- Repositories serve almost as a storage for your code. If you keep the remote repository up to date, you won’t lose your code if any technical difficulties arise like getting a new computer.

To update the remote repository, we use three (3) commands in this order:

1. `git add .`
2. `git commit -m “[COMMIT MESSAGE]”`
    - A commit message is like a note to the team that gives a short description of the code that’s being pushed up.
3. `git push`

Now that we know the steps to pushing code to the remote repository, let’s push up *hello_world.py* to the python-work repository. First we are going to enter a command to tell Git to store our username and password credentials. This way, it won’t need to be input each time code is pushed up. In your terminal, enter :

1. `cd python-work`
2. `git config --global credential.helper store`
3. and lastly, `git pull`

Now we can push our code to the remote repository. To reiterate, the three steps are:
1. `git add .`
2. `git commit -m “My first commit”`
    - “My first commit” is the commit message
3. `git push`

