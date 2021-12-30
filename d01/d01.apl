inp ← ⍎⍤1⊢↑⊃⎕NGET'input.txt'1
f ← {+/>⌿↑(⍺↓⍵) ⍵}
1 f inp ⍝ star 1
3 f inp ⍝ star 2