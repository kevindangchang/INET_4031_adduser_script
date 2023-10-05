#!/usr/bin/python3
import os 
import re
import sys

def main(): 
    for line in sys.stdin:
        match = re.match('#', line) 
        fields = line.strip().split(':')
        # if the line starts with '#' or the length of fields is not equal to 5 we skip it
        if match or len(fields) != 5:
            continue 
        username = fields[0]
        password = fields[0] 

        gecos = "%s %s,,," % (fields[3], fields[2])
        # seperates the forth indexed items on fields on comas if the string contains a coma
        groups = fields[4].split(',')
        print("==> Creating account for %s..." % (username))
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)

        #print cmd
        #os.systems runs cmd
        os.system(cmd)
        print("==> Setting the password for %s..." %(username))
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)
        #print cmd 
        os.system(cmd)
        #the for loop iterates through the array groups 
        for group in groups: 
            if group != '-': 
                print("==> Assiging %s to the %s group..." %(username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                #print cmd
                os.system(cmd)

if __name__ == '__main__':
    main()
