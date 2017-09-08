import requests
from decimal import Decimal
import json
import time
from rpcclient import *
import sys

def getHistory(addr, pid=31, offset=0):
  bal=getbalance_MP(addr,pid)['result']
  info=getinfo()['result']
  bal=Decimal(bal['balance'])
  
  print "Generating Address balance report for "+str(addr)
  print "Note: This will take a while. Please be patient"
  print ""
  print "Block "+str(info['blocks'])+" - Date: "+str(time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(time.time())))+" - Balance: "+str(bal)

  s=time.time() - 10
  while True:
    while (time.time() - s) < 10:
      time.sleep(1)
    
    r=requests.get("https://blockchain.info/rawaddr/"+str(addr)+"?offset="+str(offset))
    s=time.time()
    if r.status_code != 200:
      print r
      break

    resp=r.json()
  
    for tx in resp['txs']:
      for o in tx['out']:
        if o['script'][:11]=="6a146f6d6e69" or (o.get("addr")!=None and o['addr']=='1EXoDusjGwvnjZUyKkxZ4UHEf77z6A5S4P'):
          rawtx=gettransaction_MP(tx['hash'])['result']
          if rawtx['valid'] and rawtx['propertyid']==pid:
            if rawtx['sendingaddress']==addr:
              amount = Decimal(rawtx['amount'])
            else:
              amount = -Decimal(rawtx['amount'])
            block = rawtx['block']
            td = str(time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(rawtx['blocktime'])))
            print "Block "+str(block)+" | TxHash: "+str(tx['hash'])+" | Date: "+str(td)+"\t| Balance: "+str(bal)+" ("+str(amount)+" transfered)"
            #print ""+str(block)+"|"+str(tx['hash'])+"|"+str(td)+"|"+str(bal)+"|"+str(amount)+""
            bal += amount
          break

    offset += len(resp['txs'])
    if offset >= resp['n_tx']:
      break


if __name__ == "__main__":
  if len(sys.argv) != 3:
    print "Invalid number of arguments"
    print "Call with: python getHistory.py address propertyid"
  addr=str(sys.argv[1])
  pid=int(sys.argv[2])
  getHistory(addr,pid)
