# battery-stats
A system tray app for instant battery percentage, color-coded status, and notifications. Simplify your battery monitoring.

Description:
============
The project is a system tray application that provides real-time information about your computer's battery status. It uses the PyQt5 library for the graphical user interface and integrates with system resources and notifications. The application displays a battery icon in the system tray, and the icon's color and text change dynamically based on the battery's charge level and power status. Additionally, it notifies the user when the battery is fully charged or reaches a critically low level. Users can access an "Exit" option from the system tray menu to close the application.
The project offers a convenient way for users to monitor their laptop's battery status and receive important notifications, helping them manage their device's power more effectively.

Key Features:
=============
Real-time battery percentage display in the system tray.
Dynamic color and text changes based on the battery's status.
Notifications for full charge and critically low battery.
Simple system tray menu with an "Exit" option for ease of use.

Different Status:
=================

When your battery percent is less than 10: (RED color)
![less_than_10](https://github.com/a-s-akash/battery-stats/assets/149227673/03affbec-89ca-499b-ae90-32c24a6f7d29)
[definitely you need to plug in]

When your battery percent is less than 30: (ORANGE color)
![less_than_30](https://github.com/a-s-akash/battery-stats/assets/149227673/d31ca782-ec16-4b82-bbca-f3e85ae8c8e4)
[its the safer zone to plug in]

When your battery percent is more than 30: (GREEN color)
![more_than_30](https://github.com/a-s-akash/battery-stats/assets/149227673/bc35d7b1-f603-496d-ba2b-a39f2acd2cbf)
[for battery percent 30-100]

While plugged in: (BLUE color)
![while_plugged](https://github.com/a-s-akash/battery-stats/assets/149227673/dab73108-27ce-4662-b341-a323d99cc716)
[remains same color for all battery level why plugged in]

Get Notified when your battery fully charged:
![when_fully_charged](https://github.com/a-s-akash/battery-stats/assets/149227673/dde0450b-ab3d-4a38-88b5-169b7c8d37c2)
[you may unplug the charger]

