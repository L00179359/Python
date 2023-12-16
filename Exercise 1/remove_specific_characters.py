'''
Strings Functions
Coding with Strings Functions to remove specific characters  By: Rahul Kharade
20OCT2023
'''
text_with_brackets = "(IaC is subject help to understand basic of programming)"
text_without_brackets = text_with_brackets.strip ('(')
text_without_brackets = text_without_brackets.strip (')')
print(text_without_brackets)