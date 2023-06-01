#%%
import os


package_name = "com.games.fairyadventure"
pid = "applovin_int"
material = input("media:")
gaid = "734e18a1-7fe8-4945-80fa-148e1b4d3474"


stand = "https://app.appsflyer.com/{package_name}?pid={pid}&c={material}&advertising_id={gaid}".format(package_name=package_name,pid=pid,material=material,gaid=gaid)

# os.system('adb shell input text {stand}'.format(stand=stand))
print('adb shell input text {stand}'.format(stand=stand))
import qrcode
qrcode.make(stand)