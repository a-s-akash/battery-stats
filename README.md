# battery-stats
A system tray app for instant battery percentage, color-coded status, and notifications. Simplify your battery monitoring.

Description:
============
The project is a system tray application that provides real-time information about your computer's battery status. It uses the PyQt5 library for the graphical user interface and integrates with system resources and notifications. The application displays a battery icon in the system tray, and the icon's color and text change dynamically based on the battery's charge level and power status. Additionally, it notifies the user when the battery is fully charged or reaches a critically low level. Users can access an "QUIT" option from the system tray menu to close the application.
The project offers a convenient way for users to monitor their laptop's battery status and receive important notifications, helping them manage their device's power more effectively.
When you hover over the icon in the system tray, this application provides at-a-glance information about your laptop's battery status. It clearly indicates whether your battery is 'Gaining' (charging) or 'Draining' (discharging), ensuring you stay informed about the current power situation.
Right-clicking on the icon in the system tray allows you to access a menu, providing an option to quit the app.

Key Features:
=============
Real-time battery percentage display in the system tray.
Dynamic color and text changes based on the battery's status.
Notifications for full charge and critically low battery.
Offers a simple system tray interface for ease of use.

Different Status:
=================

When your battery percent is less than 10: [definitely you need to plug in]

![less_than_10](https://github.com/a-s-akash/battery-stats/assets/149227673/03affbec-89ca-499b-ae90-32c24a6f7d29)
(RED color)

When your battery percent is less than 30: [its the safer zone to plug in]

![less_than_30](https://github.com/a-s-akash/battery-stats/assets/149227673/d31ca782-ec16-4b82-bbca-f3e85ae8c8e4)
(ORANGE color)

When your battery percent is more than 30: [for battery percent 30-100]

![more_than_30](https://github.com/a-s-akash/battery-stats/assets/149227673/bc35d7b1-f603-496d-ba2b-a39f2acd2cbf)
(GREEN color)

While plugged in: [remains same color for all battery level when plugged in]

![while_plugged](https://github.com/a-s-akash/battery-stats/assets/149227673/dab73108-27ce-4662-b341-a323d99cc716)
(BLUE color)

Get Notified when your battery fully charged: [you may unplug the charger]

![when_fully_charged](https://github.com/a-s-akash/battery-stats/assets/149227673/5ec13b47-3d67-4cef-8e63-146ac3bf4956)

Get Notified when your battery level is low: [Useful to prevent from shutting down]

![low](https://github.com/a-s-akash/battery-stats/assets/149227673/cf0427e5-e50a-4d39-ad19-900d6a74a886)
(it's better to plugin at this point)

![critical](https://github.com/a-s-akash/battery-stats/assets/149227673/4e9d1bb8-601b-45c8-8b08-95e087e7054e)
(it's must to plugin)

Tooltip text: [shows the battery status with percentage]

![draining](https://github.com/a-s-akash/battery-stats/assets/149227673/67257d67-e6c4-40cd-a997-ef79e6182544)

![gaining](https://github.com/a-s-akash/battery-stats/assets/149227673/b58c15e3-23f2-4303-8585-2bbb3df375a0)
(on hover the icon)

Quit the App: [Right-click on the icon to quit the app]

![exit](https://github.com/a-s-akash/battery-stats/assets/149227673/871108f5-9299-45ab-b77f-bdcbf32821b1)


