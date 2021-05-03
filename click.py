import sys
import subprocess as sp

if(len(sys.argv) != 2):
     print("Incorrect Usage")
     print("Usage: python3 click.py <file containing subdomains>")
     sys.exit()

sp.run("mkdir poc", shell=True)
inputFile = open(sys.argv[1],"r")
i=1

for line in inputFile:
     line=line.rstrip("\n")

     content="<html>\n<head>\n<title>Clickjacking PoC</title>\n</head>\n<body>\n<h3>Copy and paste this URL into your PoC, if clickjacking exists:</h3>\n"
     content+="<h1>"+line+"</h1>\n"
     content+="<iframe src=\""
     content+=line+"\" width=100% height=100% style=\"opacity: 0.5;\"></iframe>"
     content+="\n</body>\n</html>"

     outFileName="poc/"
     outFileName+="file"+str(i)+".html"
     i+=1
     outFile=open(outFileName,"w")
     outFile.write(content)
     outFile.close()

     content=""

inputFile.close()