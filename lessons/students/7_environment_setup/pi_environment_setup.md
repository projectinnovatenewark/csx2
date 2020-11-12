<div align=center><h1>Environment Setup</h1></div>

The purpose of this section is to introduce you to the following concepts: 
- Version Control
- Visual Studio Code
- Git
- GitHub
- Bash and Aliases

<div align=center><h3>Visual Studio Code</h3></div>

In computing, **source code** is any collection of code that is written using a human-readable programming language, usually as plain text.

**Visual Studio (VS) Code** is a free source-code editor made by Microsoft for Windows, Linux and macOS. A **source-code editor** is a text editor program that is specialized for writing software.  

<div class=mdImage align=center>
    <img src="./images/5_vs_code.png" width="500" height="auto" />
</div>
<br>

**Extensions** are add-ons that allow you to customize and enhance your experience in Visual Studio by adding new features or integrating existing tools. An extension can range in all levels of complexity, but its main purpose is to increase your productivity and cater to your workflow.

<div class=mdImage align=center>
    <img src="./images/7_python.png" width="100" height="auto" />
    <img src="./images/8_highlight.png" width="100" height="auto" />
</div>

<h4>Installing Extensions</h4>
To install the Visual Studio Code extensions we will be using in this course, open VS Code and go to the extensions tab on the left.

<div class=mdImage align=center>
    <img src="./images/13_vs_eode_extensions.png" width="300" height="auto" />
</div>

First search ‘Highlight' and click Install.

<div class=mdImage align=center>
    <img src="./images/12_python-extension.png" width="300" height="auto" />
</div>

Then search ‘Python’ and click Install.

<div class=mdImage align=center>
    <img src="./images/12_python-extension.png" width="300" height="auto" />
</div>

<div align=center><h3>Version Control</h3></div>

**Version control** is a system that records changes to a file or set of files over time so that you can recall specific versions later.

In software development, a **repository** is a central file storage location. A **branch** is a version of a repository that can act as an independent line of development. A repository can contain multiple branches, which means there are multiple versions of the repository. 

<div align=center><h3>Git</h3></div>

**Git** is a distributed version-control system for tracking changes in source code during software development.

<div class=mdImage align=center>
    <img src="./images/9_git.png" width="300" height="auto" />
</div>

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

<div class=mdImage align=center>
    <img src="./images/10_github_logo.jpeg" width="300" height="auto" />
</div>
<div class=mdImage align=center>
    <img src="./images/6_github.png" width="500" height="auto" />
</div>

<div align=center><h3>Using GitHub, VS Code, and Git</h3></div>

<div ><h4>Creating the Programming Folder</h4></div>

Open the Pi's file manager, which is the icon at the top of your screen of two folders overlapping. Then, right click where the other visible folders are. Click "New Folder..." and call your folder "programming" (please note the lowercase "p", as folders are case-sensitive).
> The file path will be "home/pi/programming"

Now open up a VS Code Window. If it is not open already from installing the extensions, you can open the window by clicking the Raspberry Pi Icon in the top left of the screen -> Accessories -> Code - OSS (headmelted). Inside the VS Code window, click "Open Folder". Single click on your "programming folder" and click "ok" in the bottom right corner of the window.

The programming folder will be used as the main location in which you save everything coding related. Before moving on, change your working directory to the programming folder in your VS Code window by first opening a terminal using "CTRL + Shift + ~". Then, inside the terminal, execute `cd programming`. You can check to make sure you successfully changed your working directory using what command?

<div ><h4>Creating a New Repository</h4></div>

## FIXME: Add steps to create a repo in Github (login to Github, click "+" followed by new repository, name the repository, no README initialized, continue to next steps once youre on the page of your empty repo).

<div ><h4>Configuring a Repository</h4></div>

## FIXME: Add steps to copy/paste the code block from new repo, go through logging into GH from the command line.

<div ><h5>Error Handling</h5></div>

## FIXME: Address possible errors for the above. Document the solutions. Below are two issues students encountered.

- Permission Denied

- Error does not match any refspec

<div ><h4>Adding Files to Local Repository</h4></div>

The “python-work” folder is where the student will be completing all of their coding assignments. Out of the commands listed below, which are used for creating and/or editing files? Which are used for creating folders?

- touch
- mkdir
- echo
- cat
- Or the classic right-click (two-finger click on a Mac)

<div>This is all done within your VS Code window either inside the Integrated Terminal or the file manager popout. Let's create the classic *hello_world.py* file one more time so that we can push it up to the repository. Check your working directory, and if you aren't already, change your working directory to "python-work".</div>

`pwd`
<div>Then if you need to change your working directory:</div>

`cd python-work`

<div>You can use any of the listed methods for creating and editing the file, or you can use the following commands:</div>

`cat <<EOF>> hello_world.py`
<div>then in the prompt:</div>

`print("Hello World!")`
<div>and to close the prompt:</div>

`EOF`

Now that we have a file with some contents, we are going to push this up to the remote repository.

<div ><h3>Updating Your Remote Repository</h3></div>
Updating the remote repository is best practice for a couple reasons:

- For starters, it is Git’s main function! If you don’t update the repository with the most recent changes to the code, then your team won’t have access to it to build cool apps.
- Repositories serve almost as a storage for your code. If you keep the remote repository up to date, you won’t lose your code if any technical difficulties arise like getting a new computer.

To update the remote repository, we use three (3) commands in the following order:

1. `git add .`
2. `git commit -m “[COMMIT MESSAGE]”`
    - A commit message is like a note to the team that gives a short description of the code that’s being pushed up.
3. `git push`

Now that we know the steps to pushing code to the remote repository, let’s push up *hello_world.py* to the python-work repository. First we are going to enter a command to tell Git to store our username and password credentials. This way, it won’t need to be input each time code is pushed up. In your terminal, enter:

1. `cd python-work`
2. `git config --global credential.helper store`
    - Follow any prompts that may occur
3. and lastly, `git pull`

Now we can push our code to the remote repository. To reiterate, the three steps are:
1. `git add .`
2. `git commit -m “My first commit”`
    - “My first commit” is the commit message
3. `git push`

<div align=center><h3>Bash and Aliases</h3></div>

Early in the semester we discussed that most Linux systems use a **bash** shell to receive its commands as it is the default shell on Linux. Bash is short for **B**ourne **A**gain **SH**ell. Bash is a command language interpreter for GNU operating systems. This is the reason that so many Linux systems use bash. Although other shells do exist and are associated with the GNU Project, bash is often the default interpreter for most of its operating systems including Linux, Mac OS, and Windows. 

In order to load your preferences, bash runs the contents of the **bashrc file** at each launch. This shell script is found in each user’s home directory. It’s used to save and load your terminal preferences and environmental variables.

Terminal preferences can contain a number of different things. Most commonly, the bashrc file contains aliases. **Aliases** allow the user to refer to commands by shorter or alternative names, and can be a huge time-saver for those that work in a terminal regularly. In other words, a bash alias is a means of avoiding typing a long command sequence by using an abbreviated shortcut. 

<div ><h3>Creating An Alias</h3></div>

1. To add aliases, we can append the .bashrc text file using echo. If you remember, echo appends text to the bottom of a text file if you use the format `echo “new text to append” >> someFile.txt`. THe first command we are going to add as an alias will replace `git add .`
> How does this impact the staging area?

Next, in the command line enter:
`echo "alias gadd='git add .'" >> /home/pi/.bashrc`

Use the command `cat /home/pi/.bashrc` to confirm the change was made.

We can repeat this process for the following to commands for pushing up code. The terminal commands would look like the following:

`echo "alias gommit='git commit -m'" >> /home/pi/.bashrc`
> Note: A commit message is still needed (in quotes) to be input by a student when the alias is used.
`echo "alias gush='git push'" >> /home/pi/.bashrc`

2. It is also possible to make changes to the .bashrc through the GUI. Click on your file manager in the top left corner of your Pi’s screen. You’ll see something like the following screenshot. Click view and then “Show Hidden” to reveal the hidden files on your Pi.

You will then find the text file .bashrc. Open it and scroll to the bottom where you see our current commands.

Another common command used with Git is `git pull`, which updates your local repository from the remote repository.
- This is especially needed when working with a team on a project.

<div>Add a new line after the gush alias and enter:</div>

`alias gull =’git pull’`

You can also create aliases for non-Git related commands. One example of this is the `clear` command. This linux command clears out the terminal to make it easier to read for the next commands. An easy alias for this would be `c`. Go ahead and try to add this one on your own and the teacher will help in a couple minutes.

3. To start using your new bash aliases, close your terminal in VS Code and open a new one. Now that we have a fresh terminal, let’s change directories into “python-work” and open hello_world.py using `nano` and add the following code `print(“Goodbye World!”).
Close and save the changes you made to the file.
Now that we have changes to push up, let’s use our three new aliases to make changes to our remote repository. 

1. `gadd`
2. `gommit “Saying goodbye”`
    - Yes, we still need a commit message

3. `gush`

Now if you go to your github page at github.com/[YOUR USERNAME]/python-work, you can see your changes were made.

<div align=center><h2>Section Review Questions</h2></div>

1. **Version control is:**
    <div><b>a.</b> A programming language. (A)</div>
    <div><b>b.</b> A hardware component used to manage memory and storage. (W)</div>
    <div><b>c.</b> A system that records changes to a file or set of files over time so that you can recall specific versions later. (S)</div>
    <div><b>d.</b> An operating system. (H)</div>
    <br>

2. **Visual Studio code is a free _______ made by Microsoft.**
    <div><b>a.</b> Interpreter (I)</div>
    <div><b>b.</b> Text editor (K)</div>
    <div><b>c.</b> Calculator (S)</div>
    <div><b>d.</b> Source-code editor  (E)</div>
    <br>

3. **Extensions are add-ons that allow you to customize and enhance your experience in Visual Studio by adding new features or integrating existing tools. True or False?**
    <div><b>a.</b> True (C)</div>
    <div><b>b.</b> False (C)</div>
    <br>

4. **Git Push is used to upload _____ repository content to a ____ repository.**
    <div><b>a.</b> Remote, local (S)</div>
    <div><b>b.</b> Local, remote (R)</div>
    <div><b>c.</b> Local, local (D)</div>
    <div><b>d.</b> Remote, remote (Z)</div>
    <br>

5. **Which of the following statements are true about bash Aliases? (Choose 2)**
    <div><b>a.</b> Aliases allow the user to refer to commands by shorter or alternative names. (E)</div>
    <div><b>b.</b> Aliases are distributed version-control systems for tracking changes in source code during software development. (J)</div>
    <div><b>c.</b> Aliases are not stored in the bashrc file. (M)</div>
    <div><b>d.</b> Aliases can be a huge time-saver for those that work in a terminal regularly. (T)</div>
    <br>

**If You Have Me, You Will Want To Share Me. If You Share Me, You Will No Longer Have Me. What Am I? A  _ _ _ _ _ _**
