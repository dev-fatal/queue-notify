import winsdk.windows.ui.notifications as notifications
import winsdk.windows.data.xml.dom as dom

# create notification objects
nManager = notifications.ToastNotificationManager
notifier = nManager.create_toast_notifier(r"C:\Python310\python.exe") # put your python path there.

# define the xml notification document.
tString = """
<toast scenario='urgent'>
    <visual>
        <binding template='ToastGeneric'>
            <text>Solo Shuffle Queue!</text>
        </binding>
    </visual>

    <actions>
        <action content='Dismiss' arguments='action=dismiss'/>
    </actions>
</toast>
"""

# load the xml document.
xDoc = dom.XmlDocument()
xDoc.load_xml(tString)
notification = notifications.ToastNotification(xDoc)

# display notification
def show_windows_notification():
    notification = notifications.ToastNotification(xDoc)
    notifier.show(notification)