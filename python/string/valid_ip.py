class Solution:
    def validIPAddress(self, IP: str) -> str:
        def v4(s):
            res=s.split(".")
            return len(res)==4 and all(i and (not i.startswith("0") or i=="0") and all(j.isdigit() for j in i) and 0<=int(i)<256 for i in res)
        def v6(s):
            res=s.split(":")
            return len(res)==8 and all(i and len(i)<=4 and all(j in "0123456789abcdefABCDEF" for j in i) for i in res)
        if v4(IP):
            return "IPv4"
        elif v6(IP):
            return "IPv6"
        return "Neither"
