# Similar-Words-Algorithm-

A small web service for printing similar words in the English language.
Two words w_1 and w_2 are considered similar if w_1 is a letter permutation of w_2 (e.g., "stressed" and "desserts").

### To run the code:
Run the script using
```docker build -t gutsy .```
```docker run -it -p 8000:8000 gusty```
The web service should be accessible at http://localhost:8000
example: http://localhost:8000/api/v1/stats

### To run the tests: 
```poetry run python -m pytest```

Note:
To install poetry ```pip install poetry``` or see https://python-poetry.org/docs/#installing-with-the-official-installer


### Algorithm description:
The implemented algorithm for the Quart web service efficiently addresses the problem of finding similar words in the English language based on letter permutations. 
The module first initializes a global dictionary variable by reading words from the "words_clean.txt" file, Assuming each line in the text file represents a word.
For each word in the file, the _sort_chars helper function is utilized to obtain the sorted representation of its characters. This sorted representation serves as a key in a defaultdict, organizing words with similar permutations together.
The initialization process ensures efficient access to words based on their letter permutations. The module provides functions to find similar words to a given input word, checking for their presence in the dictionary. Additionally, it offers a function to retrieve the total number of words in the dictionary. The module incorporates a global variable to store the total number of words, and an exception, WordNotFound, is raised when a word is not found during the search process. 
The get_total_words function simply returns the precomputed total number of words, which is stored in a global variable. This operation has a time complexity of O(1) because it involves a direct retrieval of a stored value.
The logic is designed to optimize the runtime efficiency of word retrieval and organization, supporting the overall responsiveness of the Quart web service.
Statistics has attributes to store the total number of requests, the total processing time in nanoseconds, and the start time of each request. The start_processing method is called at the beginning of each request, recording the start time and incrementing the total request count. The end_processing method is called at the end of each request, calculating the processing time by subtracting the start time from the current time, and updating the total processing time. The get_avg_processing_time_ns method calculates and returns the average processing time per request in nanoseconds, ensuring a minimum value of 1 to avoid division by zero.

API endpoints:
The /api/v1/similar endpoint processes requests to find words in the dictionary that are permutations of the provided word.
The /api/v1/stats endpoint calculates and returns general statistics about the program, including the total number of words, total requests, and average processing time.
In addition- The /api/v1/docs endpoint provides API documentation.

This algorithm efficiently handles requests, tracks processing time, and provides statistics about the program's performance. 
The use of asynchronous features in Quart allows the server to handle a high rate of requests and parallel processing effectively.



## Requirements
The service expect the DB (txt file) to be in the local directory with the same name.  
The web service listen on port 8000 and support the following two HTTP endpoints:

### similar 
GET /api/v1/similar?word=stressed  
Returns all words in the dictionary that has the same permutation as the word "stressed".  
The word in the query should not be returned. 

The result format is a JSON object as follows:
{
    similar:[list,of,words,that,are,similar,to,provided,word]
}

For example:
http://localhost:8000/api/v1/similar?word=apple
{"similar":["appel","pepla"]}

### stats 
GET /api/v1/stats  
Return general statistics about the program:
1. Total number of words in the dictionary
1. Total number of requests (not including "stats" requests)
1. Average time for request handling in nano seconds (not including "stats" requests)

The output is a JSON object structured as follows:
{
    totalWords:int
    totalRequests:int
    avgProcessingTimeNs:int
}

For example:
http://localhost:8000/api/v1/stats
{"totalWords":351075,"totalRequests":9,"avgProcessingTimeNs":45239}


## Misc / hints:
1. Please shortly describe the algorithm you use to solve the problem as part of the submission.
2. Use any popular programming language you like, but please do think about CPU and memory optimization or the possible trade-offs. 
3. Please try to keep the solution as simple as possible. 
4. The words file remains static throughout the execution of the server. It doesn’t change. 
5. Please write the task under Linux dev environment.
6. Please do expect a high rate of requests and requests arriving in parallel.
7. Please write all errors/logs to stdout/stderr.
8. There is no need to keep any persistent state between runs. Each new run starts completely clean.
9. The program should be submitted as a complete package with instructions on how to build and run it (including the source code). You can use Github (or similar) but please make the repo private in this case.  
