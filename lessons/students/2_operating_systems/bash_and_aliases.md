Helpful Lesson to Optimize Your Command Line and Git Flows!!!
Before you start this, please make sure to check that when you copy/paste the echo commands, your single quotes ' don't change to other characters. Slack has a nasty habit of messing with quotes!
For those that use bash as their command line language interpreter (should be everyone as it includes Mac and PC's), you can create shortcut commands by utilizing your "bash_profile" file. The bash_profile file stores your "PATH" variables as well as custom aliases and custom functions.
-------------------------------------------------------------------------------------------------------------------------------------------------------
For example on PATH, when you run a python file in the terminal by running python app.py, the command you use to run "app.py" is stored in your PATH. Whether you enter py app.py, python app.py, or python3 app.py depends on the version of Python you installed and which command it stores in your PATH. No matter which of those three commands you run, they all serve the same purpose- they tell your computer where the Python program is located so it can be used to execute your Python file!
-------------------------------------------------------------------------------------------------------------------------------------------------------
For example regarding aliases, are you like one of our many students that has had an awful a fun time remembering our git commands? Well, fear no more! You can save custom commands using bash_profile aliases. Below is a command you can enter in your terminal to directly create aliases in your bash_profile using a Linux command, "echo", assuming that your bash_profile is store on your user.
echo 'alias gush='git push'' >> /Users/[YOUR_USERNAME]/.bash_profile
What if we wanted to set aliases for all three commands to be executed separately?
echo 'alias ga='git add .'' >> /Users/[YOUR_USERNAME]/.bash_profile
echo 'alias gc='git commit -m'' >> /Users/[YOUR_USERNAME]/.bash_profile
echo 'alias gp='git push'' >> /Users/[YOUR_USERNAME]/.bash_profile
Then to add, commit, and push we would simply enter these three commands in our terminal when we are within the repository's working directory! (Note- to commit, you'd still have to enter the commit message after gc which we demo here).
ga is the equivalent of "git add ."
gc "commit message here" is the equivalent of "git commit -m "commit message here"
gp is the equivalent of "git push"
-------------------------------------------------------------------------------------------------------------------------------------------------------
For example using functions, what if we wanted to combine all three commands that we use to push code up to our remote repository's branch (like a student should after completing a lesson)? Theres git add ., git commit -m "enter your commit message here, and git push (also, if you created a new branch in github that you havent pushed up to yet, you'd have to copy/paste the command that git gives you in the terminal that appears after the "git push: command to set the upstream for that branch). Let's combine all three commands in one by using a function called "lazygit() ", capturing a user input in the terminal using "$1", and setting an alias for this function called "gultimate".
echo "function lazygit() { git add .; git commit -m \"\$1\"; git push;}" >> /Users/[YOUR_USERNAME]/.bash_profile
echo "alias gultimate=lazygit" >> /Users/[YOUR_USERNAME]/.bash_profile
Then all we'd have to run to execute all three commands is gultimate "commit message here"!! This combines all three of your git commands into one, and makes you look like a pretty bad@$$ coder :smile: (