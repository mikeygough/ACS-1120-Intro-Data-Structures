When you want to access new course materials, first be sure you've committed and pushed your recent work (run git status to check) and then pull from the course's upstream repo with: `git pull upstream master`

To avoid unnecessary merge conflicts when pulling changes from upstream, write all of your project code inside the `Code` folder and do not modify or delete any existing files outside of the `Code` folder that may change upstream.

#### misc learnings..

`wc /usr/share/dict/words`

the `wc` ( word count ) command will show the number of lines, words & bytes in a file

Use the `tail` command to see what the end of the file looks like.

`tail -5 /usr/share/dict/words`

### reference:

#### virtual environments

Create a Python3 Virtual Environment:
`python3 -m venv env`

Activate the Virtual Environment:
`source env/bin/activate`

Deactivate the Virtual Environment:
`deactivate`

To Remove a Virtual Environment:
`sudo em -rf venv`

#### flask

`python app.py`
