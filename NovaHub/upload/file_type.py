import filetype
import os


def main(file):
    kind = filetype.guess(file)

    if kind is None:
        if file[-4:] == ".txt":
            print("txt")
            return
        print('Unknown')
        return

    # print("Here man:------->", file[-4:])
    print("Type:-----> ", type(kind.extension))
    print('File extension: %s' % kind.extension)
    print('File MIME type: %s' % kind.mime)


# path = "C:\\CloudDriveProject\\NovaHub\\filetypes"
# directory = os.scandir(path)
# for file in directory:
#     print(file)
#     main(file.path)
#     print("----------")

def fun(*args, **kwargs):
    print(args[0])


class Person:
    # def __init__(self):
    #     self.name = "temp"
    name = "No"
    @property
    def full_name(self):
        return self.name

    @full_name.setter
    def full_name(self, name):
        self.name = name

# a = Person()
# print(a.name)
# a.name = "Bob"
# print(a.name)

# filetypes_dir = os.getcwd() + "\\" + "filetypes\\"
#
# print(filetypes_dir)
# with os.scandir(filetypes_dir) as currentdir:
#     for file in currentdir:
#         print(filetypes_dir)
