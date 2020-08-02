#!/bin/bash
if [[ $# -eq 0 ]] ; then
    echo 'É preciso informar a mensagem de commit. Abortando...'
    exit 1
fi

# git clone https://github.com/ActiveConclusion/COVID19_mobility.git

cd notebooks
#python countries_data_aggregator.py
python data_engineering.py
python analysis.py
python brazil_analysis.py
python saoPaulo_analysis.py
python prediction.py
python brazilian_prediction.py
# python saoPaulo_prediction.py

tar -cvzf data/incoming_data.gz data/brazil_corona19_data.csv data/gov_brazil_corona19_data.xlsx data/world_corona19_data.csv
rm data/brazil_corona19_data.csv 
rm data/gov_brazil_corona19_data.xlsx data/world_corona19_data.csv
cd ..
git add .
git commit -m "$1"
git push
