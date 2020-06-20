class Solution(object):
     def BKhome(self, moves):
        if moves == "":
            return True
        numu = 0
        numr = 0
        for i in range(len(moves)):
             if moves[i] == 'U':
                 numu += 1
            elif moves[i] == 'D':
                 numu -= 1
             elif moves[i] == 'R':
               numr += 1
            else:
                 numr -= 1
        if numu == 0 and numr == 0:
             return True
        else:
             return False


 if __name__ == '__main__':
     solution = Solution()
     print(solution.BKhome("UD"))