<div align=center><h1>Section 6: Using the Command Line</h1></div>

The purpose of this section is to introduce you to the following concepts: 
- Reviewing the commands you already know.
- Learning new commands and how they work.

<div align=center><h2>Review the Commands We Know</h2></div>

- The command to check what working directory you are in is `pwd`
- You can use `ls` to list the contents of your current working directory
- To change your working directory, use `cd folderName` or to move up one level in the structure, use `cd ..`
- Create directories with `mkdir folderName`
- Create blank files with `touch fileName.fileType`
- Delete files with `rm fileName` and delete folders using the “-r” flag such as
`rm -r folderName`

<div align=center><h2>New Commands</h2></div>

Click <a href="https://cocalc.com/doc/terminal.html">here</a> to go back into the terminal emulator from the last lesson as we will be using it again to learn some new commands. In the previous lesson, we learned how to create empty files using touch. There is a way to create and write to text files with contents in the same command though using “echo”. “echo” uses the following structure:
`echo “Whatever text you want in quotes” > newFile.txt`

Let’s create a text file called *newFile.txt* with the contents reading “Echo is a great tool to create and write to text files.”

This command should look like the following:
`echo “Echo is a great tool to create and write to text files.” > newFile.txt`

Notice the structure of using only one “>” in the command. This is for when you are writing to empty files (or want to overwrite an entire file.) If you want to add to a text file, we can use two arrows like “>>”. Use the following to add “Adding to the text file.” to the end of newFile.txt.
`echo “Adding to the text file.” >> newFile.txt`

Want to check if this was a success? Well there is a command for reading files! We can use `cat fileName` to read the contents of the files without actually opening it. In your terminal, enter the following:
`cat newFile.txt`.

You should see the following output in your terminal:

<div class=mdImage align=center >
    <kbd>
        <img src="./images/emulator1.png" width="auto" height="400" />
    </kbd>
</div>
<br>

“cat” is short for”concatenate” and is a powerful command that can be utilized in many ways. Similar to what we just used “cat” for, we can display the contents of files with their line numbers showing. Our first line in newFile.txt should be **“Echo is a great tool to create and write to text files.”** and the second line will be **“Adding to the text file.”** This is done by using the “-n” flag as such:
`cat -n newFile.txt`

“cat” is also great for creating files to write to other than text files. Here we will use the “cat” command to create a file named *hello_world.py* and in that we will create a python program to display the phrase “Hello World!” This is a common programming practice when learning about programming.

In your terminal execute the following command:
`cat <<EOF>> hello_world.py`

Followed by entering the following into the terminal and hitting enter:
`print(“Hello World!”)`

Lastly type in `EOF` and hit enter. Here “EOF” is used to indicate to the terminal that we are finished editing the file.

Notice the structure of our command:
1. The terminal recognizes “cat” and looks for what comes next
2. <<EOF>> signifies for the input following the command to be added to the end of the file. 
3. You specify which file you want to add to
4. Add whatever contents you’d like to the file (you can add multiple lines too!)
5. Use `EOF` to close the file editor

Now use the “cat” command to read the file’s contents using:
`cat hello_world.py`

Let’s test out our python file by using `python3 hello_world.py`. “python3” is how you can run python files from your terminal to see their output. We are expecting our program to have an output of “Hello World!”. Your terminal should look like the following after running the python file.

<div class=mdImage align=center >
    <kbd>
        <img src="./images/emulator2.png" width="auto" height="400" />
    </kbd>
</div>
<br>

Lastly, you can use the “cat” command from earlier to add to the end of files. Let’s add another print statement to hello_world.py that when executed outputs “Goodbye World!”

To do so, we will execute the following in the terminal:
`cat <<EOF>> hello_world.py`
`print(“Goodbye World!”)`

Use the “cat” command to read hello_world.py and make sure the command executed correctly: `cat hello_world.py`

Then run the python file using `python3 hello_world.py`. You should see the following output:

<div class=mdImage align=center >
    <kbd>
        <img src="./images/emulator3.png" width="auto" height="400" />
    </kbd>
</div>
<br>

<div align=center><h2>…More Commands!</h2></div>

We have been working in the terminal from the outside of files while using “cat”. Though it would be useful to be able to edit files in the terminal inside a file. Well… there is a command for that. The “nano” command allows you to open files and directly edit them.

In your terminal, enter the following:
`nano hello_world.py`

You’ll see the following screen:

<div class=mdImage align=center >
    <kbd>
        <img src="./images/emulator4.png" width="auto" height="400" />
    </kbd>
</div>
<br>
Here you can edit files with little restriction!

> Do keep in mind though you still need to navigate solely with your keyboard as the mouse will not do much for you here.

Let’s add another print statement after our original “Hello World!” that will read “It’s great to see you.” To do so, use your keyboard to navigate to the end of the first print statement and hit enter. Then you will have a new line between the two print statements.

On that line enter the following:
`print(“It’s great to see you.”)`

Now to close the file press the “control” key and “X” key at the same time. You’ll see the following screen:

<div class=mdImage align=center >
    <kbd>
        <img src="./images/emulator5.png" width="auto" height="400" />
    </kbd>
</div>
<br>

Press “Y” to save the changes you made and then press the “enter” key. Let’s test our file to see if it worked. In the terminal now, enter:
`python3 hello_world.py`. If everything was done successfully, you should see the following:

<div class=mdImage align=center >
    <kbd>
        <img src="./images/emulator6.png" width="auto" height="400" />
    </kbd>
</div>
<br>

Now that we have “cat” and nano, let’s take a look at a more advanced command such as **sed**. This command works like a find and replace inside a file that you specify. The commands structure would look like the following:
`sed ‘s/word_to_replace/new_word/#_of_times_to_replace’ file_name`

Create a text file in your programming folder named “cat_hat.txt” using the command `touch cat_hat.txt`. Then use cat to edit the file and paste in the text from <a href="https://docs.google.com/document/d/1TlJmCw_FUclphlJ1VVqAFKsNduzV4bVXwzfsDbccnws/edit">here</a>. This is the famous Cat in the Hat story from Dr. Seuss. We are going to replace “cat” in the story with “bat” using the **sed** command.

In your terminal now, enter the following command:
`sed 's/cat/bat/g' cat_hat.txt`
    1. cat is the word to be replaced
    2. bat is the word replacing cat
    3. “g” is used to signify to the terminal to replace every instance where cat is used.
        - If you wanted every other “cat” to be replaced by “bat”, then you would put “2” instead of “g”. 
You’ll see the terminal gives you an output after executing the above command. Here you’ll see that the word “bat” has replaced “cat” in every instance.
