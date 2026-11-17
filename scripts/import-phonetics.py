"""Select only needed US IPA entries from the pinned ipa-dict TSV.
Usage: python -X utf8 scripts/import-phonetics.py path/to/en_US.txt
The input dataset is not bundled wholesale. See content/vocabulary/PHONETICS.md.
"""
import hashlib,json,re,sys
from pathlib import Path
root=Path(__file__).resolve().parents[1]
source=Path(sys.argv[1]); data=dict(line.split('\t',1) for line in source.read_text(encoding='utf-8').splitlines())
words=json.loads((root/'src/data/vocab.json').read_text(encoding='utf-8'))
needed={w['term'].lower() for w in words}|{p for w in words for p in re.findall(r"[a-z]+(?:'[a-z]+)?",w['term'].lower())}
# Spelling aliases retain the dictionary's American pronunciation and accent label.
aliases={
 'anonymise':'anonymize','artefact':'artifact','commercialisation':'commercialization',
 'customise':'customize','decentralisation':'decentralization','digitise':'digitize',
 'enrolment':'enrollment','incentivise':'incentivize','instalment':'installment',
 'marginalised':'marginalized','memorisation':'memorization','randomised':'randomized',
 'revitalise':'revitalize','stabilise':'stabilize','synchronise':'synchronize','urbanisation':'urbanization'
}
selected={term:data[term] for term in sorted(needed) if term in data}
for term,alias in aliases.items():
 if term in needed and alias in data:selected[term]=data[alias]
out={'source':'https://github.com/open-dict-data/ipa-dict/blob/972cd67dd5f96bc5660e28070cde26e3928abcd7/data/en_US.txt','revision':'972cd67dd5f96bc5660e28070cde26e3928abcd7','sourceSHA256':hashlib.sha256(source.read_bytes()).hexdigest(),'accent':'General American','license':'MIT (ipa-dict/cmudict-ipa); CMUdict BSD-style notice retained','entries':dict(sorted(selected.items()))}
(root/'content/vocabulary/phonetics-us.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
missing=sorted(p for p in needed if ' ' not in p and '-' not in p and p not in selected)
print('Selected',len(selected),'dictionary entries; add reviewed supplements for:',missing)
