import os

os.system("sudo yum update -y")
os.system("sudo yum install httpd -y")

hostname = os.popen("hostname").read().strip()
html = f"<html><body><h1>Servidor Web: {hostname}</h1></body></html>"

with open("/var/www/html/index.html", "w") as f:
    f.write(html)

os.system("sudo systemctl start httpd")
os.system("sudo systemctl enable httpd")