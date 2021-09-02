# Git reset and git revert

## Git reset
- It changes the commit history, so use it when the changes are only in local
- It will move the HEAD to the indicated commit and discard anything after
- The `--soft` option means that you will not loose the uncommitted changes you may have
- If you want to reset to the last commit and also remove all unstaged changes, yo can use the `--hard` option.

Examples:
```
git reset --soft HEAD~1

git reset --hard HEAD~1
```

## Git revert
- It will create a commit that reverts the changes of the commit being targeted.
- Doesn't overwrite the commit history

Example

```
git revert <commit_to_revert>
```