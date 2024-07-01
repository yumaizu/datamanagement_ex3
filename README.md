# Task 1 (10 points). Heads or Tails
1. Create a new Git repository.

.2 Use any programming language to write a simple “Heads or Tails” game. The program imitates 3 rounds of coin tossing by generating and printing five random Heads/Tails values on the screen:

```
Tossing a coin...
Round 1: Heads
Round 2: Tails
Round 3: Tails
Heads: 1, Tails: 2
```

3. Commit this program as your first revision with the message “HoT: initial revision”.

4. Create a separate branch called user_name. Modify the program in this branch so it asks the user to provide a name first, and then greets the user as follows:

```
Who are you? 
> John
Hello, John!
```
After greeting the user, the program imitates coin tossing exactly as in the previous version. Commit this new revision with the message “User name added”.

5. Add the following code to the master branch: if heads win, the program prints the message You won, otherwise it prints the message You lost. Commit this revision with the message “Victory message added”.

6. Merge user_name branch into the master branch. Change the code so it prints the user name instead of You. Thus, the resulting dialog would look like this:

```
Who are you? 
> John
Hello, John!
Tossing a coin...
Round 1: Heads
Round 2: Tails
Round 3: Heads
Heads: 2, Tails: 1
John won!
```

7. Commit this new revision with the message “Final revision”. Your current branch should be master.

# Submission Instructions.
1. Create a GitHub account for yourself.
2. Upload your code to GitHub.
3. Provide the link to your GitHub repository on the exercise submission page.
