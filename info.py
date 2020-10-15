#! /usr/bin/python3

if __name__ == '__main__':
    from mtec_presence_tracing import load_user_data, print_user_data
    print('Stored default user data')
    print_user_data(load_user_data())
