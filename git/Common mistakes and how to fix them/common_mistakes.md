# Common mistakes and how to fix them


## 1. Spelled last commit message wrong
```
git commit --amend
```

Opens a new editor and lets you change the last commit message.

<br>

## 2. Spelling mistake on branch name
```
git branch -m <old_branch_name> <new_branch_name>
```

If you already push the branch then you need to:
```
git push origin --delete <old_branch_name>
git push origin <new_branch_name>
```

<br>

## 3. Accidentally committed all changes to the master branch

```
git branch <new_branch>
git reset HEAD~ --hard
git checkout <new_branch>
```
Make sure you commit or stash your changes first, or all will be lost!

This creates a new branch, then rolls back the master branch to where it was before you made changes, before finally checking out your new branch with all your previous changes intact.

<br>

## 4. Forgot to add a file to that last commit
```
git add <file>
git commit --amend
```

<br>

## 5. Added a wrong file in the repo
If all you did was stage the file and you haven’t committed it yet, it’s as simple as resetting that staged file:
```
git reset <file>
```
If you have gone as far as committing that change, no need to worry. You just need to run an extra step before:
```
git reset --soft HEAD~1
git reset <file>
git commit
```
This will undo the commit and then add a new commit in its place.

<br>

## 6. Shift-Deleted a file
```
git checkout -- <file>
```
This will bring back the last committed version of test.txt from your repo.

Important: Only last committed version of the file is returned - any local changes you made before deletion are lost and any un-versioned files are not recovered.

Now the syntax is a bit weird as -- is used without an option. But this is just a workaround so that git can distinguish between branch names and files names (for branches, you would use git checkout branch-name).

<br>

## 7. Reverting pushed commit
```
git revert <commit_hash_id> -m "<commit_message>"
```
This does not remove your commit from history. It only adds another commit that reverts the changes.

<br>
<br>
<br>

<hr>



<small>
Sources:
<ul>
    <li>
        <a href="https://medium.com/@iAnkurBiswas/common-git-mistakes-and-how-to-fix-them-10184cd5fa77">Common mistakes and how to fix them
        </a>
    </li>
    <li>
        <a href="https://dev.to/abh1navv/fixing-basic-mistakes-with-git-4m4l">Fixing basic mistakes with Git 
        </a>
    </li>
</ul>
</small>
