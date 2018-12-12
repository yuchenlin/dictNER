# dictNER: a simple dictionary-based method for NER

This script collects an entity dictionary from the training data and directly uses the dictionary to label the testing sentences. It is useful when one would like to know how well this simple method can work on a NER data set. We show the results on some well-known NER datasets.

## Usage:
``python train-dict-ner.py /path/to/training_data /path/to/test_data``


## Results: 

- CoNLL 2003 English NER

```angular2html
processed 46665 tokens with 5648 phrases; found: 3535 phrases; correct: 2670.
accuracy:  89.62%; precision:  75.53%; recall:  47.27%; FB1:  58.15
              LOC: precision:  79.76%; recall:  75.36%; FB1:  77.50  1576
             MISC: precision:  75.47%; recall:  63.53%; FB1:  68.99  591
              ORG: precision:  76.12%; recall:  45.88%; FB1:  57.25  1001
              PER: precision:  55.86%; recall:  12.68%; FB1:  20.67  367
```

- OntoNotes 5.0 NER (11 names)

```angular2html
processed 230118 tokens with 8446 phrases; found: 11089 phrases; correct: 4581.
accuracy:  94.76%; precision:  41.31%; recall:  54.24%; FB1:  46.90
            EVENT: precision:  41.11%; recall:  43.53%; FB1:  42.29  90
              FAC: precision:  22.95%; recall:   9.40%; FB1:  13.33  61
              GPE: precision:  57.59%; recall:  80.60%; FB1:  67.18  3563
         LANGUAGE: precision:  47.37%; recall:  40.91%; FB1:  43.90  19
              LAW: precision:  10.91%; recall:  13.64%; FB1:  12.12  55
              LOC: precision:  22.09%; recall:  33.49%; FB1:  26.62  326
             NORP: precision:  58.50%; recall:  66.77%; FB1:  62.36  1130
              ORG: precision:  33.43%; recall:  38.96%; FB1:  35.99  2333
           PERSON: precision:  28.53%; recall:  42.08%; FB1:  34.00  3148
          PRODUCT: precision:  17.54%; recall:  22.22%; FB1:  19.61  114
      WORK_OF_ART: precision:  12.80%; recall:  18.93%; FB1:  15.27  250
```


- OntoNotes 5.0 NER (11 names + 7 values)

```angular2html
processed 230118 tokens with 12586 phrases; found: 25664 phrases; correct: 6075.
accuracy:  87.21%; precision:  23.67%; recall:  48.27%; FB1:  31.76
         CARDINAL: precision:   2.22%; recall:  24.98%; FB1:   4.08  11303
             DATE: precision:  35.29%; recall:  49.02%; FB1:  41.04  2482
            EVENT: precision:  38.16%; recall:  34.12%; FB1:  36.02  76
              FAC: precision:  20.69%; recall:   8.05%; FB1:  11.59  58
              GPE: precision:  57.92%; recall:  80.60%; FB1:  67.40  3543
         LANGUAGE: precision:  47.37%; recall:  40.91%; FB1:  43.90  19
              LAW: precision:   9.26%; recall:  11.36%; FB1:  10.20  54
              LOC: precision:  22.15%; recall:  33.49%; FB1:  26.67  325
            MONEY: precision:  44.44%; recall:  16.90%; FB1:  24.49  135
             NORP: precision:  58.50%; recall:  66.77%; FB1:  62.36  1130
          ORDINAL: precision:  13.84%; recall:  19.32%; FB1:  16.13  289
              ORG: precision:  33.80%; recall:  38.56%; FB1:  36.02  2284
          PERCENT: precision:  64.22%; recall:  51.47%; FB1:  57.14  327
           PERSON: precision:  29.02%; recall:  41.85%; FB1:  34.27  3077
          PRODUCT: precision:  20.62%; recall:  22.22%; FB1:  21.39  97
         QUANTITY: precision:  15.38%; recall:   9.15%; FB1:  11.48  91
             TIME: precision:  22.90%; recall:  30.22%; FB1:  26.05  297
      WORK_OF_ART: precision:  40.26%; recall:  18.34%; FB1:  25.20  77
```

- W-NUT 2016 NER 

```angular2html
processed 61908 tokens with 3473 phrases; found: 661 phrases; correct: 312.
accuracy:  90.81%; precision:  47.20%; recall:   8.98%; FB1:  15.09
          company: precision:  69.79%; recall:  10.79%; FB1:  18.69  96
         facility: precision:   0.00%; recall:   0.00%; FB1:   0.00  6
          geo-loc: precision:  62.27%; recall:  23.02%; FB1:  33.61  326
            movie: precision:   0.00%; recall:   0.00%; FB1:   0.00  1
      musicartist: precision:  25.00%; recall:   0.52%; FB1:   1.03  4
            other: precision:  61.29%; recall:   3.25%; FB1:   6.18  31
           person: precision:   9.09%; recall:   3.11%; FB1:   4.64  165
          product: precision:  26.32%; recall:   2.03%; FB1:   3.77  19
       sportsteam: precision:  15.38%; recall:   1.36%; FB1:   2.50  13
           tvshow: precision:   0.00%; recall:   0.00%; FB1:   0.00  0
```

## Notes

- when an entity has multiple types in the training data, we consider it to be of the most common type (when there is a tie, we take the most globally frequent one)
- the results can be different using python 3.5.x and 3.6/7.x. We use python 3.7.x to run the script.
