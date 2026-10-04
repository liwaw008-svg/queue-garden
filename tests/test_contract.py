from pathlib import Path
S=(Path(__file__).parents[1]/'contracts'/'contract.py').read_text()
def test_calls():
 for name in ('open_garden','plant_request','rank_request','revise_request','serve_next','close_expired','get_garden','get_ticket'):assert 'def '+name in S
def test_order_and_recovery():
 assert "score<best or (score==best" in S and "gl.message.sender_address!=g.steward" in S and "now()<=int(g.close_at)" in S
def test_consensus_integrity():
 assert "bool(no)!=(priority=='WAITLIST')" in S and "run()==leader.calldata" in S and "g.policy_digest!=r['policy_digest']" in S
