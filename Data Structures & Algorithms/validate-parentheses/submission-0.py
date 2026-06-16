class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {')' : '(' , 
                        '}' : '{' , 
                        ']' : '['}
        
        for c in s:
            #if close look in stack for the open
            if c in closeToOpen: #check if the element in the list before comparing
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                
                else:
                    return False #not the same element
            
            else:
                #opening element 
                stack.append(c)
        
        return True if not stack else False #return true if stack is empty
            


        

        