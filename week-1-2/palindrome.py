
def is_palindrome(s):

    def to_chars(s):
        s = s.lower()
        ans = ""
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans

    def is_pal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0]==s[-1] and is_pal(s[1:-1])

    return is_pal(to_chars(s))


if __name__=="__main__":
    print is_palindrome('hello')
    print is_palindrome('alla')
    print is_palindrome('kik ala kik')

