def isValid(self, s: str) -> bool:
        stack = []
        opening = ["(", "{", "["]
        closing = [")", "}", "]"]
        for ch in s:
            if ch in opening:
                stack.append(ch)
            if ch in closing:
                if stack:
                    top = stack.pop()
                    if ch == ")" and top != "(":
                        return False
                    elif ch == "}" and top != "{":
                        return False
                    elif ch == "]" and top != "[":
                        return False
                else:
                    return False
                
                
        return False if stack else True