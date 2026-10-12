import hashlib, json, pathlib, sys
path=pathlib.Path(sys.argv[1]); raw=path.read_bytes()
result={'input_sha256':hashlib.sha256(raw).hexdigest(),'json_valid':False,'evidence_envelope_valid':False,
        'efoa_status':'NOT_EVALUATED','semantic_accuracy':'NOT_EVALUATED','canonical_adoption':'NOT_AUTHORIZED'}
try:
  evidence=json.loads(raw)
  result['json_valid']=True
  result['evidence_envelope_valid']=isinstance(evidence,dict) and isinstance(evidence.get('evidence_id'),str) and isinstance(evidence.get('normalized_result'),(dict,list)) and not evidence.get('error') and evidence.get('success') is not False
  result['top_level_keys']=list(evidence)[:40] if isinstance(evidence,dict) else []
except Exception as exc:
  result['error']=str(exc)
print(json.dumps(result,indent=2))
if not result['evidence_envelope_valid']: sys.exit(1)
