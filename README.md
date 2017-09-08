# balanceHistory
Provide method for historical balances

# Software Requirements
* Fully synced omnicored client : https://bintray.com/omni/OmniBinaries/OmniCore/view
* Python 2.7

# Setup Requirements
Note: USER refers to the user you are running the software as

Clone this repo as the same user that is running omnicored
Ensure your Omnicored config file is setup to allow RPC connections 
 > server=1
 > rpcuser=
 > rpcpassword=

If the omnicored config file is located in a directory other than `/home/'+USER+'/.bitcoin/bitcoin.conf' `
then create a new config file in `/home/'+USER+'/.bitcoin/bitcoin.conf'` with the following 2 config lines to omnicore config:
 > rpcuser=
 > rpcpassword=

If your omnicore config file is in the same directory as `/home/'+USER+'/.bitcoin/bitcoin.conf'`
then no additional configuration files are necessary. 

# Running
`python getHistory.py address propertyid`

Example to get the Tether history (property id 31) of address 1myaddress:
`python getHistory.py 1myaddress 31`


