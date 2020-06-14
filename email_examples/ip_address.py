from ipaddress import *
import ipaddress


def _print(this):
    print(this)


def main():
    _print(ip_address('192.168.1.2'))
    _print(ip_address('2001:af3::'))


if __name__ == '__main__':
    main()

