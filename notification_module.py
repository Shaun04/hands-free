from plyer import notification

'''
Version: 1.0
^______^
'''

class NotifyMe:
    def first(title, message):

        notification.notify(
            title = title,
            message = message,
            timeout = 5,
        )

if __name__ == "__main__":
    hello = ["asdas", 'sdasdasd']
    bye = ["sdasd", "dasfdas"]
    NotifyMe.first(hello[0], bye[0])