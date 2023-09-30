class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        movey = moves.count('U') - moves.count('D')
        movex = moves.count('R') - moves.count('L')
        
        return (movey == 0 and movex == 0)
        
