class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        i = 0
        n = len(path)
        
        while i < n:
            # // (>1 '/' treat as single '/')
            while i < n and path[i] == '/':
                i += 1
            
            start = i
            while i < n and path[i] != '/':
                i += 1
            interm = path[start:i]

            # /./ (do nothing)
            if not interm or interm == '.':
                continue

            # /../ (go previous directory)
            elif stack and interm == '..':
                stack.pop()
            
            elif not stack and interm == '..':
                continue

            # /.../ (>2 '.' treat as directory name, or other weird combinations like ..home)
            else:
                stack.append(interm)
        
        return '/' + '/'.join(stack)