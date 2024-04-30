import math
import queue
from collections import Counter

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'),
              ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'),
              ('relev--ant', '-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]


def MED(S, T):
  if (S == ""):
    return (len(T))
  elif (T == ""):
    return (len(S))
  else:
    if (S[0] == T[0]):
      return (MED(S[1:], T[1:]))
    else:
      return (1 + min(MED(S, T[1:]), MED(S[1:], T)))


def fast_MED(S, T, MED={}):
  if (S, T) in MED:
    return MED[(S, T)]

  if S == "":
    return len(T)

  elif T == "":
    return len(S)
  elif S[0] == T[0]:
    result = fast_MED(S[1:], T[1:], MED)
  else:
    insertcost = fast_MED(S, T[1:], MED)
    deletecost = fast_MED(S[1:], T, MED)
    result = 1 + min(insertcost, deletecost)
    MED[(S, T)] = result
  return result


def fast_align_MED(S, T, MED={}):
  if (S, T) in MED:
    return MED[(S, T)]
  elif S == "":
    MED[(S, T)] = ("-" * len(T), T)
    return MED[(S, T)]
  elif T == "":
    MED[(S, T)] = (S, "-" * len(S))
    return MED[(S, T)]
  else:
    if S[0] == T[0]:
      S_aligned, T_aligned = fast_align_MED(S[1:], T[1:], MED)
      MED[(S, T)] = (S[0] + S_aligned, T[0] + T_aligned)
    else:
      S_insert, T_insert = fast_align_MED(S, T[1:], MED)
      S_delete, T_delete = fast_align_MED(S[1:], T, MED)

      insertcost = 1 + len(S_insert)
      deletecost = 1 + len(S_delete)

      if insertcost <= deletecost:
        MED[(S, T)] = ("-" + S_insert, T[0] + T_insert)
      else:
        MED[(S, T)] = (S[0] + S_delete, "-" + T_delete)

  return MED[(S, T)]
