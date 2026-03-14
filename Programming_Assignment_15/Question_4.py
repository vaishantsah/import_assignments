class EmailSeperator:
    def __init__(self,email:str)->None:
        self.email=email
        
    def seperator(self)->str:
        """
            Separates the username from the email address.
            
        Returns:
            - str: The username part of the email address.
        """
        if '@' not in self.email:
            return "Invalid"
        else:
            return self.email.split('@')[0].rstrip()
        
if __name__=="__main__":
    email = input("Enter the email address: ")
    email_seperator = EmailSeperator(email)
    print(email_seperator.seperator())