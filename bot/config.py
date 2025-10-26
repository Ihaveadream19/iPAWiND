api_id = 22192471 # get this from my.telegram.org
api_hash = "5812716ed49dd80b23e1d9a7856c8c64" # get this from my.telegram.org
bot_token = "7885877253:AAEzArm0SrHqcf4cBUHcLfrvN0lvm2qvrgY"  # get it from @botfather
server_address = "https://shortflare.ww4786560.workers.dev//api" # your url shortner api

PASSWORD = "1"
api_key = ""
api_urls = []

admin = [719363292] # add your telegram user ID
reseller = []

web_path = "/var/www/html"
template = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
  <dict>
    <key>items</key>
    <array>
      <dict>
        <key>assets</key>
        <array>
          <dict>
            <key>kind</key>
            <string>software-package</string>
            <key>url</key>
            <string><![CDATA[{url}]]></string>
          </dict>
          <dict>
            <key>kind</key>
            <string>full-size-image</string>
            <key>url</key>
            <string><![CDATA[{redirect_url}]]></string>
          </dict>
          <dict>
            <key>kind</key>
            <string>display-image</string>
            <key>url</key>
            <string><![CDATA[{redirect_url}]]></string>
          </dict>
        </array>
        <key>metadata</key>
        <dict>
          <key>bundle-identifier</key>
          <string><![CDATA[{package_name}]]></string>
          <key>bundle-version</key>
          <string>1.0.0</string>
          <key>kind</key>
          <string>software</string>
          <key>title</key>
          <string>{appname}</string>
        </dict>
      </dict>
    </array>
  </dict>
</plist>"""


accounts = [
]

reseller_accounts = {
}


excluded_accounts = (

)
