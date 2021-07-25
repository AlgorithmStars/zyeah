class Solution:

    def pieceDecoding(self, piece, i, dp):
        if len(piece) == 0:
            dp[i] = 1
            return dp

        one = 0
        two = 0
        if len(piece) >= 1:
            if piece[0] == '0':
                dp[i] = 0
                return dp
            one = dp[i+1] % 1000000007
            if piece[0] == '*':
                one *= 9
        if len(piece) >= 2:
            two = dp[i+2] % 1000000007
            if piece[0:2] == '**':
                two *= 15
            elif piece[0] == '*':
                if piece[1] < '7':
                    two *= 2
            else:
                if piece[1] == '*':
                    if int(piece[0]) > 2:
                        two = 0
                    elif int(piece[0]) == 2:
                        two *= 6
                    elif int(piece[0]) == 1:
                        two *= 9
                else:
                    if int(piece[0:2]) > 26:
                        two = 0
        dp[i] = (one % 1000000007 + two % 1000000007) % 1000000007
        return dp

    def numDecodings(self, s: str) -> int:
        dp = [-1 for i in range(len(s)+1)]
        for i in range(len(s), -1, -1):
            dp = self.pieceDecoding(s[i:], i, dp)
        return dp[0]
