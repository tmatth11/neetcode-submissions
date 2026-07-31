class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join([str(len(s)) + "#" + s for s in strs])

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
            