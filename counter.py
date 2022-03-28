def countEmail():
    # This first line is provided for you
    name = input("Enter file:")
    dictionary_email = dict()
    maximum = 0 
    address_max = ''

    #open file
    if len(name) < 1 : name = "mbox-short.txt"
    handle = open(name)

    #looks for 'From ' lines and takes the second word of those lines as the person who sent the mail
    for line in handle: 
        words = line.split()
        if len(words) < 2 or words[0] != 'From': #skip lines that we don't want to look at
            continue 
        else: 
            if words[1] not in dictionary_email: 
               dictionary_email[words[1]] = 1 #checking for 1st 
            else: 
                dictionary_email[words[1]] += 1 #adding counts

    for email in dictionary_email: #find the max email and count
        if dictionary_email[email] > maximum: 
            maximum = dictionary_email[email]
            address_max = email

    print(address_max, maximum) #prints email associated with max email count

#countEmail()
        


    
        
## if you want to test locally before you try to sync
## uncomment countEmail() and run > python counter.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
##countEmail()
