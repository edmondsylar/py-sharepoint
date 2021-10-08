from shareplum import Office365, version
from shareplum import Site
from shareplum.site import Version

# credentials and additional data
url = 'https://cloudprodsolutions.sharepoint.com/'
username = 'edmondmusiitwa@centebank.onmicrosoft.com'
password = 'Sylar963(0)'

# site
s_site = 'https://centebank.sharepoint.com/sites/ScannedUploads'

authcookie = Office365(url, username, password).GetCookies()
site = Site(s_site, version=Version.v365, authcookie=authcookie)
folder = site.Folder('Local Uploads')

# lets upload the file from here.
with open('up.png', mode='rb') as file:
    fileContent = file.read()
    folder.upload_file(fileContent, 'up.png')


def upload_sharepoint(file_):
    # function for uploading files to 
    # sharepoint online.
    pass