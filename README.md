<p align="center">
<img src="files/bitmass_logo.PNG" alt="drawing" width="300"/>
</p>

<hr>
 <h3 align="center">Multiple Weaknesses  Checking for Mass Subdomains</h3>
 
<p align="center">
  <a href="https://github.com/Leoid/B1tMass/releases">
    <img src="https://img.shields.io/github/release/Leoid/B1tMass/all.svg">
  </a>
  <a href="https://travis-ci.com/Leoid/B1tMass">
    <img src="https://img.shields.io/travis/com/Leoid/B1tMass.svg">
  </a>
 <a href="https://github.com/Leoid/B1tMass/issues?q=is%3Aissue+is%3Aclosed">
      <img src="https://img.shields.io/github/issues-closed-raw/Leoid/B1tMass.svg">
      </a>
      </a>
 <a href="https://www.gnu.org/licenses/gpl-3.0">
      <img src="https://img.shields.io/badge/License-GPL%20v3-blue.svg">
  </a> 
</p>

<p align="center">
<img src="files/sample2.PNG" alt="drawing" />
</p>
<p align="center">
<img src="files/sample3.PNG" alt="drawing" />
</p>


### Main Features
* Checking Live Hosts
* Checking DOM XSS
* Checking CORS Vulnerabilities
* Checking Header Injection

## Usage
```python3 b1tmass.py [-h] [-f FILE] [-O ORIGIN] [-c] [-H] [-D] [-t THREADNUMBERS]```

### Optional Arguments:
  * -h, --help            show this help message and exit
  * -f FILE, --file FILE  Subdomains File Path
  * -O ORIGIN, --origin ORIGIN
                        Origin Tag to be Injected
  * -c, --cors            CORS Checking
  * -m, --mobile          Mobile Mode
  * -z, --fuzz            Searching for File/s in all subdomains
  * -H, --headers         Headers Injection Checking
  * -D, --dom             DOM XSS Checking
  * -t THREADNUMBERS, --threads THREADNUMBERS
                        Number of Threads



## Contribution, Credits & License
### Ways to contribute

* Suggest a feature
* Report a bug
* Fixing Issues

Licensed under the GNU GPLv3, see LICENSE for more information.
