# -*- coding: utf-8 -*-

def list_all_links(page):
    
    '''
    It's a string / argument / parameter page as input, and treating page as a
    page of HTML, returns a list of strings for each URL in page.
    '''
    
    list_container = []
    
    #list_container is an empty list that will hold all the links from the 
    #"page" whenever a link is found and appended to list_container
    
    increment = 0
    
    #Increment is used for page_start to show certain parts of "page." 
    #Increment will change as the while loop continues. Whenever a link is
    #found, the program will take the index of the first letter of that link
    #based on where it's found on "page." This will then slice any string
    #before the link found and show the strings after the first index of the 
    #link found all the way until the end.
    
    page_start = page[increment:]
    
    #page_start will substitute the argument in the function "page." This will
    #take the index value from increment and print all the other strings after
    #that index number from increment (which changes in the while loop in
    #"increment = raw_link_index")
    
    href_tag = page_start.find('<a href="')
    
    
    #href_tag is used to find the string '<a href="', which in this case is
    #where the links will be found withing "page." This will give the index
    #number of the first index in '<a href="' (which will be '<') that is found 
    #within "page."
    
    while href_tag != -1:
        
        #If href_tag can't find '<a href="' within "page," then it will give 
        #back a value of -1. If given -1 as a value for href_tag, then it will
        #move to the else statement, which will return a -1. If href_tag is
        #found withing "page," it will be true for the while loop as it does
        #not equal to -1, but instead an index number that is positive found 
        #within "page"
        
        first_quote = page_start.find('"', href_tag)
    
        #first_quote will find the first quotation mark starting from the
        #string href_tag. This will give back the index value of that quotation
        #mark found within "page"
        
        second_quote = page_start.find('"', first_quote + 1)
       
        ####################################################################
        #second_quote will find the second quotation mark starting from the
        #string first_quote with an additional index number. So it doesn't read
        #the first_quote as the second_quote. This will give back the index 
        #value of that quotation mark found within "page"
        
        grab_link = page_start[first_quote + 1:second_quote]
       
        #grab_link will only string slice the first quote (with an additional
        #index number to not include '"') till the end of the second_quote.
        # print(grab_link)
        # print()
        grab_link_index = page_start.find(grab_link)
        
        #grab_link_index gives the index value of the first character/letter
        #within grab_link 
        
        increment = grab_link_index
        
        #increment within the function stores the value from grab_link_index,
        #which should also change the value of increment that is found outside
        #of the while loop so it changes the content in page_start by string 
        #slicing page[271:] (Note: page[271:] is the beginning character/letter
        #within the first link found so it would print the first link and the
        #rest of "page" after). {ISSUE: The issue in this code is that it seems
        #like the while loop is not looping, while also slicing "page" with
        #page_start and having the function continue seraching for another link
        #to append list_container to store all links found.}
        
        # [INCREMENT IS BEING UPDATED]
        
        page_start = page_start[increment:]
        
      
        # [PAGE_START IS BEING UPDATED]
        
        ##################################################################
        list_container.append(grab_link)
        
        #This line of code will take the link found in grab_link and append it 
        #to the empty list in list_container.
        
        #######################################################################
        
        href_tag = page_start.find('<a href="')
        
    return list_container









