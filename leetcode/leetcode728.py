class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []
        
        for n in range(left,right+1):
            divn = True
            
            if '0' in str(n):
                divn = False
                continue 
                
            for d in str(n):
                if n % int(d) != 0:
                    divn = False
                    break
                    
            if divn:
                result += [n]
        
        return result
