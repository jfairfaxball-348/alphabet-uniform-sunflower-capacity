import json,subprocess,sys,unittest
from pathlib import Path
R=Path(__file__).resolve().parents[1]
class GovernanceTests(unittest.TestCase):
    def test_full_validator(self):
        subprocess.run([sys.executable,str(R/"scripts/validate.py")],check=True)
    def test_no_premature_proofs(self):
        d=json.loads((R/"authoritative/STATE.json").read_text())
        self.assertFalse(d["headline_proved"])
        self.assertFalse(d["new_uniform_exponent_improvement"])
        self.assertEqual(d["new_theorems"],0)
    def test_separate_project_handoff(self):
        t=(R/"sessions/NEXT_SESSION.md").read_text()
        self.assertIn("NEW ChatGPT Project",t)
        self.assertIn("Parent S005",t)
        self.assertIn("fixed delta",t)
    def test_scope_guard(self):
        t=(R/"authoritative/CLAIMS.md").read_text()
        self.assertIn("r=3",t)
        self.assertIn("FALSE",t)
if __name__=="__main__":unittest.main()
