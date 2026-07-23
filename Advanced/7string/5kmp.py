def longestSuffixPrefix(txt):
    lps=[]*len(txt)
    lps[0]=0
    i=1
    ln=0
    n=len(txt)
    while i<n:
        if txt[i]==txt[ln]:
            ln+=1
            lps[i]=ln
            i+=1
        else:
            if ln==0:
                lps[i]=0
                i+=1
            else:
                ln=lps[ln-1]

def kmpSearch(strs,pat):
    n,m=len(strs),len(pat)
    lps=longestSuffixPrefix(pat)
    i,j=0,0
    res=[]
    while i<n:
        if strs[i]==pat[j]:
            i+=1
            j+=1
        if j==m:
            res.append(i-j)
            j=lps[j-1]
        elif i<n and strs[i]!=pat[j]:
            if j!=0:
                j=lps[j-1]
            else:
                i+=1
    return res















class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        lps = [0] * len(needle)

        prevLPS, i = 0, 1
        while i < len(needle):
            if needle[i] == needle[prevLPS]:
                lps[i] = prevLPS + 1
                prevLPS += 1
                i += 1
            elif prevLPS == 0:
                lps[i] = 0
                i += 1
            else:
                prevLPS = lps[prevLPS - 1]

        i = 0  # pointer for haystack
        j = 0  # pointer for needle

        while i < len(haystack):
            if haystack[i] == needle[j]:
                i, j = i + 1, j + 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j - 1]

            if j == len(needle):
                return i - len(needle)

        return -1