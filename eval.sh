export DATASET=~/Dataset
export RESULT=./result
export TOKENIZERS_PARALLELISM=true

python -u experiments/evaluate.py --dataset $DATASET/t17 --method clust --output $RESULT/reclust.json > log.txt