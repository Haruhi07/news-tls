DATASET=dataset
HEIDELTIME=venv/lib/python3.8/site-packages/tilse/tools/heideltime
CODE=preprocessing

python $CODE/preprocess_tokenize.py --dataset $DATASET/t17
python $CODE/preprocess_heideltime.py --dataset $DATASET/t17 --heideltime $HEIDELTIME
python $CODE/preprocess_spacy.py --dataset $DATASET/t17