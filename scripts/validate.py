#!/usr/bin/env python3
import json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
def run():
    s=json.loads((R/"authoritative/STATE.json").read_text())
    m=json.loads((R/"project_manifest.json").read_text())
    d=json.loads((R/"sessions/S002/DECISION.json").read_text())
    assert s["repo"]==m["repository"]=="jfairfaxball-348/alphabet-uniform-sunflower-capacity"
    assert s["repository_id"]==m["repository_id"]==1419073216
    assert s["parent"]==m["parent_repository"]=="jfairfaxball-348/sunflower-structures-programme"
    assert s["last_mathematics_session"]=="P001C-S002" and "P001C-S002" in m["last_completed_session"]
    assert s["stage"]==d["stage"]=="RETURN_PARENT_PAUSE_NO_D_EXPONENT_MECHANISM"
    assert s["next_session"]==m["next_session"]=="SUN-PARENT-S006"
    assert s["decision"]==d["decision"]=="NO"
    assert s["next_executed"] is False and m["next_executed"] is False
    assert s["child_S003_queued"] is False and d["new_child_session_queued"] is False
    assert s["new_uniform_exponent_improvement"] is False and d["new_uniform_exponent_improvement"] is False
    assert s["D_independent_base_proved"] is False and s["headline_proved"] is False
    assert s["new_theorems"]==m["new_theorems"]==d["new_claimed_theorems"]==0
    assert s["formal_status"]==s["publication_status"]=="NOT_STARTED"
    assert d["entry_main"]=="519d70b20162e219f628b90d2cf3de4c62d9a209"
    prompt=(R/"sessions/NEXT_SESSION.md").read_text()
    for k in ("PAUSED","NO child S003","SUN-PARENT-S006","separately"):
        assert k in prompt,k
    x=(R/"sessions/S002/RESEARCH.md").read_text()
    for k in ("RETURN_PARENT / PAUSE","2n/3","7/12","5/8","one-hot","perfect-matching","Fourier","Hegedus","UNPROVED","D^(-epsilon*n)"):
        assert k.lower() in x.lower(),k
    y=(R/"sessions/S001/RESEARCH.md").read_text()
    for k in ("NO BOUND IMPROVEMENT","U(D,2)=4","perfect matching","one-hot","2n/3","Alon","triangular"):
        assert k.lower() in y.lower(),k
    for file in ("AGENTS.md","sessions/S000/CLOSEOUT.md","sessions/S001/INPUT_AUTHORITY.md","sessions/S002/INPUT_AUTHORITY.md","sessions/S002/CLOSEOUT.md","sources/REGISTER.md","authoritative/CLAIMS.md",".github/workflows/research-integrity.yml"):
        assert (R/file).is_file(),file
    print("PASS P001C-S002 | decision NO | RETURN_PARENT / PAUSE | no S003")
if __name__=="__main__":run()
