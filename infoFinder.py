import os


def get_info(content):

    msg = []

    for filename in os.listdir("info"):
        with open("info/" + filename, encoding="utf8") as f:

            paragraph = ""

            for line in f:

                paragraph += line

                if end_of_paragraph(line):
                    if content_is_in_paragraph(content, paragraph):
                        msg.append(paragraph.replace(',', " ") + "\n Found in " + filename + "\n" + \
                              "----------------------\n")
                    paragraph = ""

    if len(msg) == 0:
        msg = ["I couldn't find anything on the subject"]

    return msg


def end_of_paragraph(line):
    return line.replace(",", "") == "\n"


def content_is_in_paragraph(content, paragraph):
    words = get_words_from_content(content)

    for word in words:
        if word.lower() not in paragraph.lower():
            return False

    return True


def get_words_from_content(content):
    # Optionals "" will be read as-is. Other words are seperated with spaces

    if '"' not in content:
        return content.split(" ")

    words = content.split(" ")

    returnedValue = []

    found = False
    temp = ""

    for word in words:
        if '"' in word and not found:
            temp = word.replace('"', "")
            found = True
        elif '"' in word and found:
            temp += " " + word.replace('"', "")
            found = False
            returnedValue.append(temp)
        elif '"' not in word and found:
            temp += " " + word
        else:
            returnedValue.append(word)

    return returnedValue


def test():
    print(get_words_from_content('Hello my old friend'))
    print(get_words_from_content(''))
    print(get_words_from_content('Hello "my old" friend'))
    print(get_words_from_content('"Hello my   old friend"'))
