 
 #Finding_unique_number_of_emails
 #Rule-1: There will be no '.' in the local name
 #Rule-2: in the local name, no str will be added after '+' sign. 
def numUniqueEmails(emails):
    unique_email=set()
    for email in emails:   
        #spliting the local & domain name
        local_name,domain_name=email.split('@')
        #applying rule1 & rule2 
        local_name=local_name.split('+')[0].replace('.','')
       
        unique_email.add(local_name+'@'+domain_name)
    #returning the length of the unique emails
    return len(unique_email)

#Different types test cases
x=["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
print(numUniqueEmails(x))