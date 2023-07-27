from plyer import notification

def notifyme(title,message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "C:\\Users\\Gurwinder singh\\Downloads\\clock_time_5025.ico",
        timeout = 10,
    )

if __name__ == '__main__':
    notifyme("hey guri,you should take a break now ","You should follow 20-20-20 rule for keep your eyes healthy")