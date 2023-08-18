import random
import string


    
chars_after_at=(random.randint(5,8))
letters_list =[string.digits,string.ascii_lowercase,string.ascii_uppercase]
    
letters_list_to_str="".join(letters_list)
email_format="@bugfoo.com"


mail="".join(random.choices(letters_list_to_str,k=chars_after_at))
emwofo=mail
emailwfo=mail+email_format

    
print(emwofo)
print(emailwfo)
        
