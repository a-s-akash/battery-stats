'''
To run the program must install these pip packages
pip install psutil
pip install plyer
pip install PyQt5
'''

import sys
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction
from PyQt5.QtGui import QIcon, QPixmap, QColor, QPainter
from PyQt5.QtCore import Qt, QTimer
import psutil
from plyer import notification

# Flags to track notification status
is_shown_full = 0
is_shown_plug = 0
is_shown_critical = 0

def battery_box(battery):
    global is_shown_full
    global is_shown_plug
    global is_shown_critical

    # Create a 16x16 pixmap for the system tray icon
    pixmap = QPixmap(16, 16)
    pixmap.fill(Qt.transparent)
    bt_text = QPainter(pixmap)

    r1, g1, b1, r2, g2, b2 = 0, 0, 0, 0, 0, 0

    # Determine text to display (battery percentage or 'F' for fully charged)
    text = f"{battery.percent}" if battery.percent < 100 else ' F'

    if battery.power_plugged:
        # Reset other notification flags
        is_shown_critical = is_shown_plug = 0
        r1, g1, b1, r2, g2, b2 = 0, 170, 255, 0, 0, 0
        if text == ' F' and is_shown_full == 0:
            # Show a notification for a fully charged battery
            notification.notify(title="Battery-Stats", message="Fully Charged (100%)", timeout=5)
            is_shown_full = 1
    else:
        if text == ' F' or int(text) > 30:
            r1, g1, b1, r2, g2, b2 = 127, 255, 0, 0, 0, 0
            if text != ' F':
                is_shown_full = 0
        elif int(text) <= 10:
            r1, g1, b1, r2, g2, b2 = 255, 0, 0, 255, 255, 255
            if is_shown_critical == 0:
                # Show a notification for a critically low battery
                notification.notify(title="Battery-Stats", message="Critically low (plug immediately)", timeout=5)
                is_shown_critical = 1
        else:
            r1, g1, b1, r2, g2, b2 = 255, 165, 0, 0, 0, 128
            if is_shown_plug == 0:
                # Show a notification to plug in to prevent critical battery level
                notification.notify(title="Battery-Stats", message="Plugin to prevent critical battery level", timeout=5)
                is_shown_plug = 1

    # Customize the system tray icon
    bt_text.setBrush(QColor(r1, g1, b1))
    bt_text.drawRect(0, 0, 200, 200)
    bt_text.setPen(QColor(r2, g2, b2))
    bt_text.drawText(3, 12, text)
    bt_text.end()

    return QIcon(pixmap)

def exit_app():
    sys.exit()

def main():
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    # Create a system tray icon
    tray_icon = QSystemTrayIcon(QIcon("icon.png"), app)
    tray_icon.show()

    timer = QTimer()

    def update_tray_icon():
        battery = psutil.sensors_battery()
        tray_icon.setIcon(battery_box(battery))

        if battery.power_plugged:
            tip_text = "G"
        else:
            tip_text = "Dr"
        tooltip_text = f"{tip_text}aining : {battery.percent}%"
        tray_icon.setToolTip(tooltip_text)

    timer.timeout.connect(update_tray_icon)
    timer.start(1000)

    # Create a right-click menu for the system tray icon
    menu = QMenu()
    exit_action = QAction("Quit")
    exit_action.triggered.connect(exit_app)
    menu.addAction(exit_action)
    tray_icon.setContextMenu(menu)

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
