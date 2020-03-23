
# Tema 1 LFA Lambda NFA

## Indicatii de implementare

1. Matricea de tranzitie δ se modifica astfel:

| δ  | a0 | a1 | a2 | λ
| -- | -- | -- | -- | -- |
| q0 | {} | {} | {} | {} |
| q1 | {} | {} | {} | {} |
| q2 | {} | {} | {} | {} |
| q3 | {} | {} | {} | {} |

2. Introducem in matricea de trazitii caracterul λ  
De tinut cont ca λ nu citeste niciun caracter din cuvant pentru a il folosi.

3. La fiecare pas cand actualizam starile curente, trebuie sa tinem cont si de starile in care ajungem cu λ tranzitie.

## Executarea:
Implimentarea automatului Lambda NFA a fost executată în limbajul de programare Python.
Pentru rularea acestuia este necesară executarea următorilor pași:
1. Clonarea directivei și deschiderea acesteia.
2. Rularea fișierului ***lambda_nfa.py*** cu ajutorul comenzii: *python3 lambda_nfa.py*