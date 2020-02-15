from lorem.text import TextLorem
def main():
    # separate words by '-'
    # sentence length should be between 2 and 3
    # choose words from A, B, C and D
    lorem = TextLorem(wsep='-', srange=(2, 3), words="A B C D".split())

    s1 = lorem.sentence()  # 'C-B.'
    s2 = lorem.sentence()  # 'C-A-C.'
    print("This is dummy gm.com text, will hit on this")
