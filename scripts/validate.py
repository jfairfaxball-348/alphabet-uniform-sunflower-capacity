#!/usr/bin/env python3
import json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
def run():
    state=json.loads((R/"authoritative/STATE.json").read_text())
    manifest=json.loads((R/"project_manifest.json").read_text())
    assert state["repo"]=="jfairfaxball-348/alphabet-uniform-sunflower-capacity"
    assert state["repository_id"]==manifest["repository_id"]==1419073216
    assert state["parent"]==manifest["parent_repository"]=="jfairfaxball-348/sunflower-structures-programme"
    assert state["next_session"]==manifest["next_session"]=="P001C-S001"
    assert state["last_mathematics_session"] is None and state["next_executed"] is False and manifest["next_executed"] is False
    assert state["new_uniform_exponent_improvement"] is False
    assert state["D_independent_base_proved"] is False and state["headline_proved"] is False
    assert state["new_theorems"]==manifest["new_theorems"]==0
    assert state["formal_status"]==state["publication_status"]=="NOT_STARTED"
    prompt=(R/"sessions/NEXT_SESSION.md").read_text()
    for text in ("P001C-S001","U(D,n)","Naslund","ASU","NEW ChatGPT Project","NO BOUND IMPROVEMENT"):
        assert text.lower() in prompt.lower(),text
    assert "r=3" in (R/"README.md").read_text() or "three petals" in (R/"README.md").read_text()
    for file in ("AGENTS.md","sources/REGISTER.md","authoritative/CLAIMS.md","sessions/S000/CLOSEOUT.md",".github/workflows/research-integrity.yml"):
        assert (R/file).is_file(),file
    print("PASS P001C administrative repository integrity; no mathematics claimed")
if __name__=="__main__":run()
