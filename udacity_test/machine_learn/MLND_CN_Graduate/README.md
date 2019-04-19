# 机器学习纳米学位
# 毕业项目
## 项目: 猫狗大战
### 安装

这个项目需要安装下面这些python包：

- [numpy]
- [pandas]
- [scikit-learn]
- [matplotlib]
- [keras]
- [opencv-python]
- [tensorflow-gpu]
- [tqdm]
- [h5py]


优达学城推荐学生安装[Anaconda](https://www.continuum.io/downloads), 

### 代码

代码包含在`graduate.ipynb`和`graduate_clean.ipynb`这两个notebook文件中，其中`graduate.ipynb`为全部数据集的训练+预测，`graduate_small.ipynb`为对训练集异常数据的清洗。还会用到`common.py`文件。


### 运行
在命令行中，确保当前目录为 包含本 README 文件，运行下列命令：

```bash
jupyter notebook graduate.ipynb
```

```bash
jupyter notebook graduate_clean.ipynb
```

​这会启动 Jupyter Notebook 并把项目文件打开在你的浏览器中。

### 数据
数据集来自https://www.kaggle.com/c/dogs-vs-cats-redux-kernels-edition。