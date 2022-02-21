def main():
    banner()
    instruction()
    sentence = input('Enter a sentence here: ')
    camelcased = CamelCase(sentence)
    print(camelcased)

def CamelCase(sentence):
    """Convert sentence to camelCase, for example, "Display all books"
    is converted to "displayAllBooks" """
    title_case = sentence.title()
    sentencesplit = title_case.split()
    sentenceList2 = ("".join(sentencesplit))
    return sentenceList2

def banner():
    """Display welcome banner"""
    message = "CAMELCASE PROGRAM!"
    stars = '*' * len(message)
    print(f'{stars}\n{message}\n{stars}')

def instruction():
    """Print instruction message"""
    print('Enter a sentence to convert to CamelCase')



if __name__ == '__main__':
    main()