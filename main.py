from gui import *


def main():
    window = Tk()
    window.title('Xbill')
    window.geometry('500x150')
    window.resizable(False, False)
    widgets = GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()
