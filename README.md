# ece208
Git repo for ECE208

Requires Python3

Run the following to print a NNF formula to stdout

```
python3 gen_form.py
```
* Positive integers are used to denote a unique proposition
* '-' is used to denote logical negation
* '.' is used to denote logical inclusive or
* '+' is used to denote logical and

For example the output: '((-3) + (1 . (-5)))' denotes:

((NEG X3) AND (X1 OR (NEG X5)))

The generator will always output a valid NNF formula that is fully parentisized. 
