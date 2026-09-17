class Solution:
    def getSum(self, a: int, b: int) -> int:
        a = list(reversed(bin(a)[2:]))
        b = list(reversed(bin(b)[2:]))

        a = [int(x) for x in a]
        b = [int(x) for x in b]

        i = j = 0
        carry = 0
        res = []

        while i < len(a) and j < len(b):
            res.append(a[i] ^ b[j] ^ carry)
            carry = a[i] & b[j] | carry
            i+=1
            j+=1

        while i < len(a):
            res.append(a[i] ^ carry)
            carry = a[i] & carry
            i+=1

        while j < len(b):
            res.append(b[j] ^ carry)
            carry = b[j] & carry
            j += 1

        if carry:
            res.append(carry)
        
        ans = 0
        for i in range(len(res)):
            ans += res[i] * pow(2, i)

        return ans

