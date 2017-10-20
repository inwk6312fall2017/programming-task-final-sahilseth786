# Simple Example of calling REST API from Python
# This is all that is required to call a REST API from python

# * THIS SAMPLE APPLICATION AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY
# * OF ANY KIND BY CISCO, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED
# * TO THE IMPLIED WARRANTIES OF MERCHANTABILITY FITNESS FOR A PARTICULAR
# * PURPOSE, NONINFRINGEMENT, SATISFACTORY QUALITY OR ARISING FROM A COURSE OF
# * DEALING, LAW, USAGE, OR TRADE PRACTICE. CISCO TAKES NO RESPONSIBILITY
# * REGARDING ITS USAGE IN AN APPLICATION, AND IT IS PRESENTED ONLY AS AN
# * EXAMPLE. THE SAMPLE CODE HAS NOT BEEN THOROUGHLY TESTED AND IS PROVIDED AS AN
# * EXAMPLE ONLY, THEREFORE CISCO DOES NOT GUARANTEE OR MAKE ANY REPRESENTATIONS
# * REGARDING ITS RELIABILITY, SERVICEABILITY, OR FUNCTION. IN NO EVENT DOES
# * CISCO WARRANT THAT THE SOFTWARE IS ERROR FREE OR THAT CUSTOMER WILL BE ABLE
# * TO OPERATE THE SOFTWARE WITHOUT PROBLEMS OR INTERRUPTIONS. NOR DOES CISCO
# * WARRANT THAT THE SOFTWARE OR ANY EQUIPMENT ON WHICH THE SOFTWARE IS USED WILL
# * BE FREE OF VULNERABILITY TO INTRUSION OR ATTACK. THIS SAMPLE APPLICATION IS
# * NOT SUPPORTED BY CISCO IN ANY MANNER. CISCO DOES NOT ASSUME ANY LIABILITY
# * ARISING FROM THE USE OF THE APPLICATION. FURTHERMORE, IN NO EVENT SHALL CISCO
# * OR ITS SUPPLIERS BE LIABLE FOR ANY INCIDENTAL OR CONSEQUENTIAL DAMAGES, LOST
# * PROFITS, OR LOST DATA, OR ANY OTHER INDIRECT DAMAGES EVEN IF CISCO OR ITS
# * SUPPLIERS HAVE BEEN INFORMED OF THE POSSIBILITY THEREOF.-->


# import requests library
import requests

#import json library
import json

controller='sandboxapic.cisco.com'
#controller='devnetapi.cisco.com/sandbox/apic_em'


# put the ip address or dns of your apic-em controller in this url
url = "https://" + controller + "/api/v1/ticket"

#the username and password to access the APIC-EM Controller
payload = {"username":"devnetuser","password":"Cisco123!"}

#Content type must be included in the header
header = {"content-type": "application/json"}

#Performs a POST on the specified url to get the service ticket
response= requests.post(url,data=json.dumps(payload), headers=header, verify=False)

#convert response to json format
r_json=response.json()

print(r_json)
#parse the json to get the service ticket
ticket = r_json["response"]["serviceTicket"]

# URL for Host REST API call to get list of exisitng hosts on the network.
url = "https://" + controller + "/api/v1/host?limit=1&offset=1"

#Content type must be included in the header as well as the ticket
header = {"content-type": "application/json", "X-Auth-Token":ticket}

# this statement performs a GET on the specified host url
response = requests.get(url, headers=header, verify=False)

# json.dumps serializes the json into a string and allows us to
# print the response in a 'pretty' format with indentation etc.
print ("Hosts = ")
#print (json.dumps(response.json(), indent=4, separators=(',', ': ')))

r_resp = response.json()

#for x in r_resp:

#print(r_resp["response"]["hostIp"])
for x in  r_resp["response"]:
  print("Host IP Address",x["hostIp"])
  print("Host MAC Address",x["hostMac"])
  print("Host MAC Address",x["hostType"])
  #print("Host IP",x["hostIp"])
  #print("Host IP",x["hostIp"])


#print("Host Name",r_resp["response"][0]["hostType"])
#print("Host IP",r_resp["response"][0]["hostIp"])
#print("Host MAc",r_resp["response"][0]["hostMac"])
#for x in r_resp:
#  print(x)
#{'response': [{'pointOfPresence': 'ae19cd21-1b26-4f58-8ccd-d265deabb6c3', 'source': '200', 'hostIp': '10.1.15.117', 'subType': 'UNKNOWN', 'hostType': 'wireless', 'connectedNetworkDeviceIpAddress': '10.1.14.3', 'connectedNetworkDeviceId': 'cd6d9b24-839b-4d58-adfe-3fdf781e1782', 'pointOfAttachment': 'ae19cd21-1b26-4f58-8ccd-d265deabb6c3', 'connectedAPName': 'AP7081.059f.19ca', 'id': '48cdeb9b-b412-491e-a80c-7ec5bbe98167', 'connectedAPMacAddress': '68:bc:0c:63:4a:b0', 'hostMac': '00:24:d7:43:59:d8', 'vlanId': '600', 'lastUpdated': '1479514114932'}], 'version': '1.0'}

#[{'id': '48cdeb9b-b412-491e-a80c-7ec5bbe98167', 'lastUpdated': '1479514114932', 
#'pointOfPresence': 'ae19cd21-1b26-4f58-8ccd-d265deabb6c3', 'vlanId': '600', 'pointOfAttachment': 'ae19cd21-1b26-4f58-8ccd-d265deabb6c3', 
#'subType': 'UNKNOWN', 'hostType': 'wireless', 'hostMac': '00:24:d7:43:59:d8', 'connectedAPMacAddress': '68:bc:0c:63:4a:b0', 
#'connectedNetworkDeviceId': 'cd6d9b24-839b-4d58-adfe-3fdf781e1782', 'hostIp': '10.1.15.117', 'connectedNetworkDeviceIpAddress': '10.1.14.3', 
#'connectedAPName': 'AP7081.059f.19ca', 'source': '200'}]

