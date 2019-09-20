import os


#os.system('python -m pip install -r requirements.txt')
#os.system("python -m pytest -s -v -n=2--setup-show -q -l -v --alluredir=reports")
os.system(r"python -m pytest  --workers 1 --tests-per-worker auto -v --setup-show tests")
#os.system('allure serve reports')
