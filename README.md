# WebFuzzer
A basic web fuzzer for engineering secure software
# How to Run
in order to run the application, please use the following format:

python fuzz [discover | test] url --common-wordlist="PATHTOFILE" OPTIONS

VALID OPTIONS

--custom-auth="WEBAPP"

TEST ONLY OPTIONS

--vectors=file

--sensitive=file

--random=[true|false]

--slow=500

only two support web apps are DVWA and boldget

Discover will only discover information regarding the given url, while test
will attempt some common exploits based on information supplied in other command line options

