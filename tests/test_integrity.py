import json,subprocess,sys,unittest,itertools
from pathlib import Path
R=Path(__file__).resolve().parents[1]
class GovernanceTests(unittest.TestCase):
 def test_full_validator(self):
  subprocess.run([sys.executable,str(R/"scripts/validate.py")],check=True)
 def test_no_claimed_improvement(self):
  s=json.loads((R/"authoritative/STATE.json").read_text())
  self.assertFalse(s["headline_proved"]);self.assertFalse(s["new_uniform_exponent_improvement"]);self.assertEqual(s["new_theorems"],0)
 def test_future_only(self):
  self.assertIn("P001C-S002",(R/"sessions/NEXT_SESSION.md").read_text())
  self.assertIn("RETURN_PARENT",(R/"sessions/NEXT_SESSION.md").read_text())
 def test_binary_cube_no_sunflower(self):
  for n in (1,2,3,4):
   A=list(itertools.product((0,1),repeat=n))
   for x,y,z in itertools.combinations(A,3):
    self.assertTrue(any(len({x[i],y[i],z[i]})==2 for i in range(n)))
 def test_sixword_balanced_capset(self):
  A=[(0,0,0),(0,0,1),(1,1,0),(1,2,2),(2,1,2),(2,2,1)]
  for i in range(3):
   self.assertEqual([sum(x[i]==v for x in A) for v in (0,1,2)],[2,2,2])
  for x,y,z in itertools.combinations(A,3):
   self.assertTrue(any(len({x[i],y[i],z[i]})==2 for i in range(3)))
 def test_exact_n2_D3(self):
  E=list(itertools.product(range(3),repeat=2))
  bad=[sum(len({E[a][i],E[b][i],E[c][i]})==2 for i in range(2))==0 for a,b,c in itertools.combinations(range(9),3)]
  tri=list(itertools.combinations(range(9),3))
  self.assertEqual(len(bad),len(tri))
  for subset in itertools.combinations(range(9),5):
   S=set(subset)
   self.assertTrue(any(z and set(t)<=S for z,t in zip(bad,tri)))
if __name__=="__main__":unittest.main()
