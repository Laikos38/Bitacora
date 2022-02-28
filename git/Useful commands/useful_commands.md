# Useful Commands

## 1. Delete local branches with deleted remote references
To update branches with remote references run:
```bash
$ git remote update --prune
```
Then:
```bash
$ git branch -vv | awk '/: gone]/{print $1}' | xargs git branch -d
```
