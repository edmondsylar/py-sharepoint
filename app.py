import requests
from requests_ntlm import HttpNtlmAuth

# file name to be uploaded.
filename = 'sample.pdf'

# Sharepoint URL.
sharePointUrl = 'https://xxxx.sharepoint.com'
folderUrl = '/sites/MyTeam/Internal'

folderUrl = '/sites/MyTeam/Internal'

requestUrl = sharePointUrl + '/_api/web/getfolderbyserverrelativeurl(\'' + folderUrl + '\')/Files/add(url=\'' + fileName + '\',overwrite=true)'
#Read in the file that we are going to upload
    
file = open(fileName, 'rb')
    
#Setup the required headers for communicating with SharePoint

headers = {'Content-Type': 'application/json; odata=verbose', 'accept': 'application/json;odata=verbose'}

#Execute a request to get the FormDigestValue. This will be used to authenticate our upload request