class Solution:
    def isPalindrome(self, s: str) -> bool:
        #for loop 
        #front and back check for same value if they are 
        no_space = "".join(filter(str.isalnum, s)).lower()
        for i in range(len(no_space)):
            if no_space[i] != no_space[-(i+1)]:
                return False
        return True

