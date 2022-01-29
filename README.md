#procedure
-----------
(language :- python)
In linux command line:-
alias parsemyjson = "/home/python parseJsonFromApi.py"  #for every time I need to fetch this release
just I need to type in command-liine->  parsemyjson
and my file will be executed

Procedure:-
1. we need one library named urllib.request to send getrequest to the url(api) and getting the response
2. first load the json
3. fetch the count of results as mentioned in the json first attribute so that we can iterate through the json file and fetch all the names of active fadora releases
4. also printing the count of total no of releases
5. making a list
6. iterate through the "results" attribute to see which release is active (means active = true)
7. now filtering the name of the release whose release is active now and appending to the list
8. printing the list into command line
