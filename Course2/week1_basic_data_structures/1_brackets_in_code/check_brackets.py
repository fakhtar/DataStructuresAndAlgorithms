# python3

# from collections import namedtuple

# Bracket = namedtuple("Bracket", ["char", "position"])


# def are_matching(left, right):
#     return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    textlen = len(text)
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append((next,i))
            if i == textlen - 1 and not not opening_brackets_stack:
                return i + 1
        else:
            if next in ")]}" and not opening_brackets_stack:
                return i+1
            if not not opening_brackets_stack:
                if next not in "([{)]}":
                    continue
                top = opening_brackets_stack.pop()[0]
                # if top in "([{" and next not in ")]}":
                if top == "(" and next != ")" or top == "{" and next != "}" or top == "[" and next != "]":
                    return i+1
    if not not opening_brackets_stack:
        return opening_brackets_stack[0][1] + 1
    return "Success"

        # if next in ")]}":
        #     # Process closing bracket, write your code here
        #     pass


def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)

# for item in [("()","Success"),("[]","Success"),("/{/}[]","Success"),("[()]","Success"),("(())","Success"),("{[]}()","Success"),("{","1"),("{[}","3"),("foo(bar);","Success"),("foo(bar[i);","10"),("[](()","3"),("(({})","1")]:
#     mismatch = find_mismatch(item[0])
#     if str(mismatch) != item[1]:
#         print("Error")
#         mismatch = find_mismatch(item[0])

if __name__ == "__main__":
    main()
