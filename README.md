# Diff_Calculator (OUTDATED)

Use https://github.com/hknio/Compare_Tool

Calculates the relative percentage difference in two given directories.

# Description
Calculates the relative percentage difference in two given directories. It was made to more easily calculate the percentage of change between commits in remediation checks of audits. It finds the percentage of change by calculating the Levenshtein distance.

# Requirements
Requirements can be installed with the following command.
```
pip3 install -r requirements.txt
```

# Usage 
Two different usage options are available:
Normal:
```
python3 main.py -p1 <PATH1> -p2 <PATH2>
```
Verbose:
```
python3 main.py -p1 <PATH1> -p2 <PATH2> -v
```
# Example Output
Normal:
![alt text](https://github.com/hknio/Diff_Calculator/blob/main/Screenshots/Screenshot%202022-11-24%20at%2022.13.53.png)

Verbose:
![alt text](https://github.com/hknio/Diff_Calculator/blob/main/Screenshots/Screenshot%202022-11-24%20at%2022.13.45.png)

# Output Details
The tool's output also lists the files that were examined. For each file, the list contains similarity percentage, difference percentage, and number of changed lines, in that order.

![alt text](https://github.com/hknio/Diff_Calculator/blob/main/Screenshots/Screenshot%202022-11-24%20at%2022.14.26.png)

# Docker 

Diff calculator now offers Docker to its users. In order to run Diff Calculator via docker one has to use the two provided scripts; build.sh and sc.sh. 

Setup Docker
```
sh ./build.sh
```
Run via Docker 
```
sh ./sc.sh <PATH1> <PATH2>
```
![alt text](https://github.com/hknio/Diff_Calculator/blob/main/Screenshots/Screenshot%202022-11-24%20at%2022.30.38.png)
