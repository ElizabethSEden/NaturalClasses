# NaturalClasses
Python program to demonstrate consequences of feature choices for a language.

Input: a JSON dictionary of segments, with feature to feature value e.g. {i:{voiced:+},s:{voiced:-}}.

Alternative input: a tab separated file in which the first line contains feature names, and the first column segment names:

       voiced    sonorant
    i    +          +
    s    +          -

To convert your tab-separated file to a JSON file, you can use csv_to_json.py from the command line.

The input filepath is specified in settings.py (not included). Output files are hard-coded.
