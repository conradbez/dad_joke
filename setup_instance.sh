cp .jupyter /home/ubuntu/.jupyter

python3 -m virtualenv .venv

source .venv/bin/activate

pip install -r requirements.txt

echo which python

ipython kernel install --user --name=.venv
