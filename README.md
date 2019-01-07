# BitdefenderExclusionsExtractor

Extract Bitdefender exclusions. This tool focuses on exclusions added to "Antivirus" only because I'm too lazy to look for the others.

How: This script uses never-seen-before XML file reading. Seriously, it's in plain text. This script just automates it for you :)

About: This was made just as a PoC. This script is built for "Bitdefender Total Security" and not the free version. I'm unsure if it would work with the free version. Also, it only extracts exclusions that are added to the "Antivirus" module and no others such as "Advanced Threat Defense". I'm unsure if you can extract exclusions from the other modules, but I assume you can somehow.

EDIT: You could also write to it if you have administrator access ;)

Note: You will probably have to edit the code. Because of this I made it easy, just change the fileLocation variable located at the top. Be sure to keep the Path() part; only modify the string. I also put enough comments in the code so if you want to understand what it's doing (it's simple stuff) you can.

Legal Notice: I did report this "issue" and they said it wasn't an issue and therefore weren't going to fix it. Also, I am not responsible for ANYTHING you do with this script.
