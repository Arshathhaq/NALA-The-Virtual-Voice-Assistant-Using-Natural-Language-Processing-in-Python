import win10toast 
from win10toast import ToastNotifier

n= ToastNotifier()
n.show_toast(title="Notification",msg="Getup buudy",duration=5,threaded=True)