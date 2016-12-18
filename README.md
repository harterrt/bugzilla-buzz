# Intro
This is a quick CLI tool that summarizes my Bugzilla activity for my weekly snippets.

The more useful your bugs are the more you'll want to keep them up to date.

# How to Use
```bash
python cli.py next
```
Lists all P1 open bugs assigned to me.
These are the bugs I plan on working on next week.
python cli.py done

```bash
python cli.py done
```
Lists all bugs I'm assigned to or CC'd on which were active since last Friday.

# Goals
* Identify all bugs I'm CC'd, Assigned, or mentioned in. (relevant bugs)
* Identify recently modified relevant bugs
* Identify zombie bugs

# Heads up
This is an early proof of concept for personal use.
Don't expect this to be stable or usable just yet.
