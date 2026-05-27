class Solution:
    def isValid(self, s: str) -> bool:
        valid_arr = []
        brack_map = {
            "}": "{",
            ")":"(",
            "]": "["
        }
        for b in s: 
            if b in brack_map:
                if valid_arr:
                    last_member = valid_arr.pop()
                    if last_member != brack_map[b]:
                        return False
                else: 
                    valid_arr.append(b)
            else:
                valid_arr.append(b)

        return True if not valid_arr else False
        