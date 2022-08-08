// https://leetcode.com/problems/defanging-an-ip-address/
// 41 ms, 13.7 MB

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")
