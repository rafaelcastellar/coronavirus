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
cd ..

gzip -kf data/brazil_corona19_data.csv 
gzip -kf data/world_corona19_data.csv 
# tar -cvzf data/incoming_data.gz data/brazil_corona19_data.csv data/world_corona19_data.csv
#cd ..
git add .
git commit -m "$1"
git push
