# Diff_Calculator
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
![alt text](https://github.com/hknio/Percentage_Calculator/blob/7f18c0b770ac7fd19cefbbcea200c3bb4faf7901/Screenshots/Screen%20Shot%202022-04-21%20at%2022.12.56.png)
Verbose:
![alt text](https://github.com/hknio/Percentage_Calculator/blob/7f18c0b770ac7fd19cefbbcea200c3bb4faf7901/Screenshots/Screen%20Shot%202022-04-21%20at%2022.13.06.png)
