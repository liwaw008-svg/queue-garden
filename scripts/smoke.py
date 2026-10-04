from pathlib import Path
import json,re,subprocess,time
from genlayer_py import create_account,create_client
from genlayer_py.chains import studionet
from genlayer_py.contracts import actions as ca
R=Path(__file__).parents[1];ROOT=R.parents[3]
def env(name):
 text=(ROOT/'accounts.env').read_text();return re.search(r'^'+re.escape(name)+r'\s*=\s*"?([^"\r\n]+)',text,re.M).group(1).strip()
def calldata(method=None,args=None,kwargs=None):
 out={}
 if method is not None:out['method']=method
 if args:out['args']=args
 if kwargs:out['kwargs']=kwargs
 return out
ca.make_calldata_object=calldata
accounts={i:create_account(account_private_key=env('ACCOUNT_'+str(i)+'_GENLAYER_PRIVATE_KEY')) for i in (2,3,4)};clients={i:create_client(chain=studionet,account=a) for i,a in accounts.items()};address=json.loads((R/'deployment.json').read_text())['contractAddress'];sha=subprocess.check_output(['git','rev-parse','HEAD'],cwd=R,text=True).strip();stamp=str(int(time.time()));garden='GARDEN-'+stamp;ticket='PRINT-'+stamp;raw='https://raw.githubusercontent.com/liwaw008-svg/queue-garden/'+sha+'/evidence/';cdn='https://cdn.jsdelivr.net/gh/liwaw008-svg/queue-garden@'+sha+'/evidence/'
def send(who,method,args):
 tx=clients[who].write_contract(address=address,function_name=method,args=args);clients[who].wait_for_transaction_receipt(transaction_hash=tx,wait_until='finalized',retries=180,interval=5000);full=clients[who].get_transaction(transaction_hash=tx);leader=(full.get('consensus_data',{}).get('leader_receipt')or[{}])[0];assert full.get('result_name')=='MAJORITY_AGREE' and leader.get('execution_result')=='SUCCESS',full;return str(tx)
txs={};txs['open']=send(4,'open_garden',[garden,accounts[3].address,'Community print workshop desk',raw+'workshop-policy.md',['Request concerns shared workshop equipment','Request identifies a public event within 72 hours','Request includes pickup and return plan'],2592000]);txs['plant']=send(2,'plant_request',[garden,ticket,cdn+'print-request.md']);txs['rank']=send(3,'rank_request',[ticket]);mid=clients[4].read_contract(address=address,function_name='get_ticket',args=[ticket]);assert mid['state']=='RANKED' and mid['priority']=='BLOOM' and mid['blocker_indexes']==[],mid;txs['serve']=send(4,'serve_next',[garden]);state=clients[4].read_contract(address=address,function_name='get_ticket',args=[ticket]);assert state['state']=='SERVED',state;out={'gardenId':garden,'ticketId':ticket,'transactions':txs,'state':state,'walletDisclosure':'All demo wallets and source fixtures are operator-controlled.'};(R/'network-run.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
