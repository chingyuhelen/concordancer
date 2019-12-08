# concordancer



## Usage

To get a file of sentences containing keywords, extracted from Chinese datasets:

```bash
python print_sents.py 擦
```

To get a file containing keywords, corresponding collocates and examples, ranked by frequencies:

```bash 
python print_freq_sents.py 破 -s 3 -hp V -d 1 -cp V N D
```
positional argument: a keyword (e.g., 擦)
optional argument:
  -s: the length of the keyword
  -hp: the part of speech(es) of the keyword
  -d: the distance between the keyword and its collocates (default = 1)
  -cp: the part of speech(es) of the collocates
  
