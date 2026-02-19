def longestSuffixPrefix(txt,lps):
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

