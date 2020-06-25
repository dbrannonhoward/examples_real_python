import faulthandler
import webbrowser

from constants.urls import FAULTHANDLER_URL


def main():
    faulthandler.enable()
    browser = webbrowser
    browser.open(FAULTHANDLER_URL)
    pass


if __name__ == '__main__':
    main()

