


def editDistanceDp(str1,str2,m,n):
   dp = [[0 for x in range(n+1)]for x in range(m+1)]
   for i in range(m+1):
	for j in range(n+1):
	    if i == 0:
		 dp[i][j] = j
	    elif j == 0:
		dp[i][j] = i
	    elif str1[i-1] == str2[j-1]:
		dp[i][i] = dp[i-1][j-1]
	    else:
		dp[i][j] = 1 + min(dp[i][j-1],        
                                   dp[i-1][j],        
                                   dp[i-1][j-1])
   print dp[m][n]

string1 = raw_input()
string2 = raw_input()

editDistanceDp(string1,string2,len(string1),len(string2))



