### 해당 프로그램을 Mac, conda+pycharm에서 실행하기

conda의 패키지들로는 실행할 수 없다.
conda환경에서 pip로 패키지들을 설치해야만 한다.

1. 실행 및 설치 환경을 위해 conda env를 activate한다.
$ conda env list
$ conda activate py09

2. 설치가 필요한 패키지들은 다음과 같다. (이미 설치 했다면, 필요없다.)
need packages: mss, pyautogui,j natsort, pynput, pyqt6, pyside6
$ pip3 install [pkg_name]

3. 실행한다.
(py09) $ which python3
(py09) $ python3 eBookToPdf.py

4. 실행이 끝나면, conda환경은 deactivate하거나 터미널을 닫는다.

EOF
