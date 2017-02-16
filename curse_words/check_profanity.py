import urllib

def read_text():
    quotes = open("C:\Python27\examples\curse_words\movie_quotes.txt")
    content_of_files = quotes.read()
    #print(content_of_files)
    quotes.close()
    check_profinity(content_of_files)

def check_profinity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check)
    output = connection.read()
    #print(output)
    connection.close()
    if "true" in output:
        print("Profinity Alert!!")
    elif "false" in output:
        print("this doc has no curse words!")
    else:
        print("Could not scan the doc properly.")

read_text()
    
