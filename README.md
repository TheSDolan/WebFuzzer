# WebFuzzer
A basic web fuzzer for engineering secure software
# How to Run
in order to run the application, please use the following format:

python Fuzzer.py discover [URL] --common-wordlist="PATHTOFILE" --options

currently the only valid --option is --custom-auth="WEBAPP"

only two support web apps are DVWA and boldget

The output from the scan will be output to stdout

