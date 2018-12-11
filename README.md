# dictNER

``python train-dict-ner.py ../NCRFpp/on_data_names/onto.train.ner.names ../NCRFpp/on_data_names/onto.test.ner.names``

- CoNLL 2003 English NER

```angular2html
processed 46665 tokens with 5648 phrases; found: 3715 phrases; correct: 2680.
accuracy:  89.30%; precision:  72.14%; recall:  47.45%; FB1:  57.25
              LOC: precision:  79.76%; recall:  75.36%; FB1:  77.50  1576
             MISC: precision:  74.51%; recall:  64.96%; FB1:  69.41  612
              ORG: precision:  65.63%; recall:  45.76%; FB1:  53.92  1158
              PER: precision:  56.10%; recall:  12.80%; FB1:  20.85  369
```

- OntoNotes 5.0 NER (11 names)

```angular2html
processed 230118 tokens with 8446 phrases; found: 61778 phrases; correct: 4750.
accuracy:  73.37%; precision:   7.69%; recall:  56.24%; FB1:  13.53
            EVENT: precision:  25.22%; recall:  34.12%; FB1:  29.00  115
              FAC: precision:   9.03%; recall:   9.40%; FB1:   9.21  155
              GPE: precision:  16.05%; recall:  81.62%; FB1:  26.82  12950
         LANGUAGE: precision:   2.50%; recall:  40.91%; FB1:   4.71  360
              LAW: precision:  19.35%; recall:  13.64%; FB1:  16.00  31
              LOC: precision:  13.63%; recall:  35.81%; FB1:  19.74  565
             NORP: precision:   3.71%; recall:  84.85%; FB1:   7.11  22653
              ORG: precision:  18.23%; recall:  37.31%; FB1:  24.50  4097
           PERSON: precision:   4.37%; recall:  41.94%; FB1:   7.92  20473
          PRODUCT: precision:  21.43%; recall:  30.00%; FB1:  25.00  126
      WORK_OF_ART: precision:  11.07%; recall:  16.57%; FB1:  13.27  253
```


- OntoNotes 5.0 NER (11 names + 7 values)

```angular2html
processed 230118 tokens with 12586 phrases; found: 86934 phrases; correct: 6648.
accuracy:  62.45%; precision:   7.65%; recall:  52.82%; FB1:  13.36
         CARDINAL: precision:   3.02%; recall:  72.34%; FB1:   5.79  24099
             DATE: precision:  10.13%; recall:  45.22%; FB1:  16.55  7977
            EVENT: precision:  30.67%; recall:  27.06%; FB1:  28.75  75
              FAC: precision:   8.00%; recall:   8.05%; FB1:   8.03  150
              GPE: precision:  19.24%; recall:  80.40%; FB1:  31.04  10642
         LANGUAGE: precision:   5.00%; recall:  40.91%; FB1:   8.91  180
              LAW: precision:  10.34%; recall:   6.82%; FB1:   8.22  29
              LOC: precision:  13.90%; recall:  33.49%; FB1:  19.65  518
            MONEY: precision:   5.31%; recall:   3.10%; FB1:   3.91  207
             NORP: precision:   4.58%; recall:  84.65%; FB1:   8.68  18315
          ORDINAL: precision:  17.02%; recall:  96.62%; FB1:  28.94  1175
              ORG: precision:  14.55%; recall:  37.46%; FB1:  20.96  5155
          PERCENT: precision:  74.73%; recall:  33.33%; FB1:  46.10  182
           PERSON: precision:   5.91%; recall:  41.89%; FB1:  10.36  15122
          PRODUCT: precision:  21.05%; recall:  22.22%; FB1:  21.62  95
         QUANTITY: precision:   0.39%; recall:   0.65%; FB1:   0.49  256
             TIME: precision:   2.53%; recall:  30.22%; FB1:   4.68  2684
      WORK_OF_ART: precision:  39.73%; recall:  17.16%; FB1:  23.97  73
```

- W-NUT 2016 NER 

```angular2html
processed 61908 tokens with 3473 phrases; found: 704 phrases; correct: 336.
accuracy:  90.83%; precision:  47.73%; recall:   9.67%; FB1:  16.09
          company: precision:  68.37%; recall:  10.79%; FB1:  18.64  98
         facility: precision:   0.00%; recall:   0.00%; FB1:   0.00  6
          geo-loc: precision:  62.27%; recall:  23.02%; FB1:  33.61  326
            movie: precision:   0.00%; recall:   0.00%; FB1:   0.00  1
      musicartist: precision:  25.00%; recall:   0.52%; FB1:   1.03  4
            other: precision:  66.67%; recall:   5.14%; FB1:   9.54  45
           person: precision:  15.14%; recall:   5.81%; FB1:   8.40  185
          product: precision:  19.23%; recall:   2.03%; FB1:   3.68  26
       sportsteam: precision:  15.38%; recall:   1.36%; FB1:   2.50  13
           tvshow: precision:   0.00%; recall:   0.00%; FB1:   0.00  0
```