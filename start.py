import os,shutil
try:
    pathforscripttwo= os.path.realpath(__file__)
    pathforscripttwo=pathforscripttwo.replace('start.py',r'\reports')
    shutil.rmtree(pathforscripttwo)
    print('file removed')
except:
    print('roports not found')
os.system('python -m pip install -r requirements.txt')
os.system(r"python -m pytest  --workers 1 --tests-per-worker auto -v --setup-show --alluredir=reports tests ")
os.system('allure serve reports')
