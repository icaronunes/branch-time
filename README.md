# Time Branch

Time Branch is a command-line interface tool that allows you to track the time you spend working on different branches in your repository. With Time Branch, you can easily monitor how much time you spend in each branch, helping you stay on top of your activities and improve productivity. Additionally, Time Branch offers features to export collected data to an output file, making it easy to analyze and share information with your team. With the help of Time Branch, you can optimize your software development activities and improve your efficiency

## Install

```bash
pip install branch-time
```

## How to use

- #### time values ​​in minutes

```bash
branchtime 'your\repository.git' --time 20 --output 'output\directory'
branchtime 'your\repository.git' -t 20 -o 'output\directory'
branchtime 'your\repository.git' --time 20 --output 'output\directory'
or
branch-time 'your\repository.git' --time 20 --output 'output\directory'
```

### default values:

- repository = your current directory
- --time = 5 minutes
- --output = your current directory

## Help

<img src="https://firebasestorage.googleapis.com/v0/b/livro-android-1327.appspot.com/o/help%20branch.PNG?alt=media&token=0739a15b-91b7-41f5-801f-1b7674f492f6">

## Output

2023-04-24.txt

```txt
Branch: master - Time: 20:57:17
FINISHED... 21:44:11

Branch: main - Time: 21:58:19

Branch: AUTO-29975 - Time: 22:10:29

Branch: AUTO-32659 - Time: 22:34:10

Branch: AUTO-31839 - Time: 23:18:46

Branch: AUTO-29975 - Time: 23:40:17

Branch: main - Time: 23:55:32
FINISHED... 23:055:33
```
