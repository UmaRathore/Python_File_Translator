# Python offline PyPi and then pip3 install translate

from translate import Translator

translator_obj = Translator(to_lang="ja")


try:
    with open('Data_for_translation.txt', mode='r') as my_file:
        text = my_file.read()
        print(text)

        translation = translator_obj.translate(text)
        print(translation)
except FileNotFoundError as err:
    print("File not present")
    print(err)
