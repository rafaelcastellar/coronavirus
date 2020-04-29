#!/bin/bash
if [[ $# -eq 0 ]] ; then
    echo 'É preciso informar a mensagem de commit. Abortando...'
    exit 1
fi

cd notebooks
#python countries_data_aggregator.py
python data_engineering.py
python analysis.py
python brazilian_analysis.py
python saoPaulo_analysis.py
python prediction.py
python brazilian_prediction.py
# python saoPaulo_prediction.py

cd ..
git add .
git commit -m "$1"
git push
