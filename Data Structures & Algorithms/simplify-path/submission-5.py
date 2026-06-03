class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        cur = ""
        for each in path + '/':
            if each == '/':
                if cur == "..":
                    if stack:
                        stack.pop()
                elif cur != '.' and cur != '':
                    stack.append(cur)
                cur = ""
            else:
                cur += each
        return '/' + '/'.join(stack)