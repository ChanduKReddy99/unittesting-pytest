
echo [$(date)]: "START"
echo [$(date)]: "creating new virtual env"
conda create --prefix ./venv python=3.8 -y
echo [$(date)]: "activating virtual env"
source activate ./venv
echo [$(date)]: "installing requirements"
pip install -r requirements.txt
echo [$(date)]: "END"

