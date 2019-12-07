## TensorFlow

### install by pip

```bash
python -m pip install pip -U
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

# or
cp pip.ini ~/pip/

python -m pip install virtualenv
# create venv
virtualenv venv  

# TensorFlow CPU
pip install tensorflow==2.0.0  
# GPU
pip install tensorflow-gpu==2.0.0    
conda install tensorflow-gpu 

pip freeze > requirements.txt
```

### conponents

```
pip install jupyter
jupyter notebook
```

## Reference

* [TensorFlow](https://tensorflow.google.cn/install)
