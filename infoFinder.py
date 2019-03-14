import os


def get_info(content):

    msg = []

    for filename in os.listdir("info"):
        with open("info/" + filename, encoding="utf8") as f:

            paragraph = ""

            for line in f:

                paragraph += line

                if line.replace(",", "") == "\n":
                    if content.lower() in paragraph.lower():
                        msg.append(paragraph.replace(',', " ") + "\n Found in " + filename + "\n" + \
                              "----------------------\n")
                    paragraph = ""

    if len(msg) == 0:
        msg = ["I couldn't find anything on the subject"]

    return msg
