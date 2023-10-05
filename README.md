# inet_4031_adduser_script
Python Script for Adding Users/Groups to a System

## Description
This Python Script reads user/group data from an input file, processes the file line-by-line and adds each user to the system.

The import os lets you talk to the operating system importing re lets you use regular expression and importing sys lets you use system commands
  
## Operation
  
### Input File Specification
  
The input file should have the following format:

*** username:default_password:last_name:first_name:comma_separated_list_of_groups

For example:

jdoe11:mypass:Doe:John:admins, reviewers

The name of the input file is up to the user.  Convention is create-users.input

### Running the Script
step 1:
```
chmod a+x create-users.py
```
step 2: 
```
sudo ./create-users.py < create-users.input
```
