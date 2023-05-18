# NR-VM_Sample.py

## Background and Usage
This script uses the CairoSVG module to show off New Relic Vulnerability Management
CairoSVG itself is a great utility that converts SVG images to other formats
CairoSVG versions before 2.7.0 had a critical CVE, which this script uses to demonstrate how New Relic VM detects security issues in your code. 
Note that the CVE was addressed in versions 2.7.0 and higher
Details on the CVE can be found here: [https://github.com/advisories/GHSA-rwmf-w63j-p7gv](https://github.com/advisories/GHSA-rwmf-w63j-p7gv)
Details on CairoSVG can be found [on their home page](https://www.courtbouillon.org/cairosvg).

## Setup: 
 - (you need a New Relic account before you start. [Get one here. They're free.](https://newrelic.com/signup) )
 - put NR-VM_Sample.py file in a directory
 - install and enable a virtual environment, container, etc. if desired.
 - install the required modules:
   - New Relic (`pip install newrelic`)
   - The vulnerable version of CairoSVG (`pip install cairosvg==2.6.0`)
 - Edit newrelic.ini
   - add your API key to the line "license_key = "
   - set your application name in the line "app_name = "

## Operation
 - At the command line, run the script (typically `python3 NR-VM_Sample.py`)
 - Go back to your New Relic dashboard and look for the application name to show up under "Entities"
 - On the side menu, click the "vulnerabilities" option
 - It may take several minutes for data to show, and for the vulnerability to display

## "Fixing" the vulnerability
 - At the command line, stop the script (Ctrl-C)
 - Run `pip install cairosvg --upgrade`
 - Restart the script
 - As with the initial detection, the resolution may take a few minutes to display in the New Relic dashboard.
