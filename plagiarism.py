# import re
# from collections import Counter


# def preprocess(code):

#     # remove comments
#     code = re.sub(r"//.*", "", code)

#     # remove multiline comments
#     code = re.sub(r"/\*.*?\*/", "", code, flags=re.DOTALL)

#     # remove package
#     code = re.sub(r"package .*?;", "", code)

#     # remove imports
#     code = re.sub(r"import .*?;", "", code)

#     # remove strings
#     code = re.sub(r'"[^"]*"', "", code)

#     return code.lower()


# def tokenize(code):

#     tokens = re.findall(
#         r"[a-zA-Z_][a-zA-Z0-9_]*",
#         code
#     )

#     return tokens


# def check_plagiarism(code1, code2):

#     code1 = preprocess(code1)
#     code2 = preprocess(code2)

#     tokens1 = tokenize(code1)
#     tokens2 = tokenize(code2)

#     set1 = Counter(tokens1)
#     set2 = Counter(tokens2)

#     common = sum(
#         (set1 & set2).values()
#     )

#     total = sum(
#         (set1 | set2).values()
#     )

#     if total == 0:
#         return 0

#     similarity = (
#         common / total
#     ) * 100

#     return round(similarity, 2)


import difflib
import re
from collections import Counter


def preprocess(code):

    # Single line comments
    code = re.sub(r"//.*", "", code)

    # Multi line comments
    code = re.sub(r"/\*.*?\*/", "", code, flags=re.DOTALL)

    # Package & imports
    code = re.sub(r"package .*?;", "", code)
    code = re.sub(r"import .*?;", "", code)

    # Strings
    code = re.sub(r'"[^"]*"', "", code)

    return code.lower()


def tokenize(code):

    return re.findall(
        r"[a-zA-Z_][a-zA-Z0-9_]*",
        code
    )


def token_similarity(code1, code2):

    tokens1 = tokenize(code1)
    tokens2 = tokenize(code2)

    counter1 = Counter(tokens1)
    counter2 = Counter(tokens2)

    common = sum(
        (counter1 & counter2).values()
    )

    total = sum(
        (counter1 | counter2).values()
    )

    if total == 0:
        return 0

    return (common / total) * 100


def sequence_similarity(code1, code2):

    return (
        difflib.SequenceMatcher(
            None,
            code1,
            code2
        ).ratio()
        * 100
    )


def check_plagiarism(code1, code2):

    code1 = preprocess(code1)
    code2 = preprocess(code2)

    token_score = token_similarity(
        code1,
        code2
    )

    sequence_score = sequence_similarity(
        code1,
        code2
    )

    final_score = (
        token_score * 0.4
        +
        sequence_score * 0.6
    )

    return round(final_score, 2)