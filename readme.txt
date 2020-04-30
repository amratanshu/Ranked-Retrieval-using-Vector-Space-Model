The Sample input file wiki_40 contains a large number of sub-documents which are returned after a Query.

Scoring Scheme - lnc.ltc 
l => Logarithm
n => normal
c => cosine

Improved the model using restriction criteria for returning relevant documents - 
a. Only High IDF 
b. Docs which contain many Query Terms
c. Both a and b

1. Run index_creation.py

2. This will populate the file dictionary.p (storing the posting lists of all the words in wiki_40)

Note - the first two steps have already been done. Warning - if you re-run the index_creation.py file, the dictionary.p file will be overwritten

3. Run test_queries.py and input the query

4. Run printDoc.py and input the docID you want to print (view the output list when you executed test_queries.py)

5. If you wish to view the improvements in working, then open test_queries.py, scroll to the last and do the following :

    a. for Improvement 1 : Change line 471 to r = returnTopDocsHIGHIDF(d,queryInput)
    b. for Improvement 2 : Change line 471 to r = returnTopDocsMANYQUERYTERMS(d,queryInput)
    c. for both together : Change line 471 to r = returnTopDocsBOTH(d, queryInput)
    
