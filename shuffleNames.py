import pandas as pd
import random 


def readexcel():
    pd.read_excel
    filename = "FirstnameLastname_fulllist.xls"
    df = pd.read_excel(filename,'names-sorted',usecols = "A,B")
    return df.values

def main():	    
    namelist = readexcel()    
    unique_email_list = []
    for item in namelist:
        firstname = item[0]
        lastname = item[1]
        emailAddress = firstname + "." + lastname
        if emailAddress not in unique_email_list:
            unique_email_list.append(emailAddress)
			
    random.shuffle(unique_email_list)
    with open('FirstnameLastname_fulllist_random.txt', 'a') as the_file:
       the_file.writelines('\n'.join(unique_email_list))
           
		
if __name__ == '__main__':
    main()