#!/usr/bin/env python3
import json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
def run():
    s=json.loads((R/"authoritative/STATE.json").read_text())
    m=json.loads((R/"project_manifest.json").read_text())
    assert s["repo"]==m["repository"]=="jfairfaxball-348/alphabet-uniform-sunflower-capacity"
    assert s["repository_id"]==m["repository_id"]==1419073216
    assert s["parent"]==m["parent_repository"]=="jfairfaxball-348/sunflower-structures-programme"
    assert s["last_mathematics_session"]=="P001C-S001"
    assert s["next_session"]==m["next_session"]=="P001C-S002"
    assert s["next_executed"] is False and m["next_executed"] is False
    assert "NO_BOUND_IMPROVEMENT" in s["stage"]
    assert s["new_uniform_exponent_improvement"] is False
    assert s["D_independent_base_proved"] is False and s["headline_proved"] is False
    assert s["new_theorems"]==m["new_theorems"]==0
    assert s["formal_status"]==s["publication_status"]=="NOT_STARTED"
    t=(R/"sessions/NEXT_SESSION.md").read_text()
    for k in ("P001C-S002","FUTURE ONLY","NO decision","D^(-epsilon n)","RETURN_PARENT"):
        assert k in t,k
    a=(R/"sessions/S001/RESEARCH.md").read_text()
    for k in ("NO BOUND IMPROVEMENT","U(D,2)=4","perfect matching","one-hot","2n/3","Alon","triangular"):
        assert k.lower() in a.lower(),k
    for f in ("AGENTS.md","sources/REGISTER.md","authoritative/CLAIMS.md","sessions/S000/CLOSEOUT.md","sessions/S001/INPUT_AUTHORITY.md",".github/workflows/research-integrity.yml"):
        assert (R/f).is_file(),f
    print("PASS P001C-S001 integrity; NO BOUND IMPROVEMENT; S002 future only")
if __name__=="__main__":run()
