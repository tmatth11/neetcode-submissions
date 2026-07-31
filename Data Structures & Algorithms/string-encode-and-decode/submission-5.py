class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []

        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        while i < len(s):
            length = ""
            # Read length of incoming string
            while s[i] != "#":
                length += s[i]
                i += 1

            length = int(length)

            # Skip #-sign
            i += 1

            # Take in incoming string
            res.append(s[i:i + length])

            i += length
        
        return res
            