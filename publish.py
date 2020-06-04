import os
os.system("cp -r dist/* .")
os.system("git add --all")
os.system("git commit -am 'update'")
os.system("git push origin master")
