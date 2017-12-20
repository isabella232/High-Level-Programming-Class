import os
import sys
# Does print print to stdout?
# we can use os.walk, right?
#print ("root prints out directories only from what you specified")
#print ("dirs prints out sub-directories from root")
#print ("files prints out all files from root and directories")

dir_to_search=sys.argv[2]
search_string=sys.argv[1]

#"/home/i-am-me/Documents/test1"
for root, dirs, files in os.walk(dir_to_search):
    #print (root)
    #print (files)
    if len(files) > 0:
        for i in range(0, len(files)):
            if search_string in files[i]:
                a=os.path.join(root, files[i])
                print (a)
