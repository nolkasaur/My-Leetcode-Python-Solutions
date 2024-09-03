# https://leetcode.com/problems/encode-and-decode-strings/
# N/A, N/A

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s)) + "%" + s
        return encoded_string

    def decode(self, s: str) -> List[str]:
        i = 0
        decoded_string = []
        while i < len(s):
            j = i
            while s[j] != '%':
                j += 1
            word_length = int(s[i:j])
            decoded_string.append(s[j+1 : j+1+word_length])
            i = j+1+word_length
        return decoded_string
