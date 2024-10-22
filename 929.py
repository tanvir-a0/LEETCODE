class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        final_email = []
        for email in emails:
            x = email
            if '+' in email:
                x = email[:email.index('+')].replace(".","") + email[email.index('@'):]
            else:
                x = email[:email.index('@')].replace(".","") + email[email.index('@'):]
            
            final_email.append(x)
            print(x)
        return len(set(final_email))
        
