
# coding: utf-8

# ## 探索电影数据集
# 
# 在这个项目中，你将尝试使用所学的知识，使用 `NumPy`、`Pandas`、`matplotlib`、`seaborn` 库中的函数，来对电影数据集进行探索。
# 
# 下载数据集：
# [TMDb电影数据](https://s3.cn-north-1.amazonaws.com.cn/static-documents/nd101/explore+dataset/tmdb-movies.csv)
# 

# 
# 数据集各列名称的含义：
# <table>
# <thead><tr><th>列名称</th><th>id</th><th>imdb_id</th><th>popularity</th><th>budget</th><th>revenue</th><th>original_title</th><th>cast</th><th>homepage</th><th>director</th><th>tagline</th><th>keywords</th><th>overview</th><th>runtime</th><th>genres</th><th>production_companies</th><th>release_date</th><th>vote_count</th><th>vote_average</th><th>release_year</th><th>budget_adj</th><th>revenue_adj</th></tr></thead><tbody>
#  <tr><td>含义</td><td>编号</td><td>IMDB 编号</td><td>知名度</td><td>预算</td><td>票房</td><td>名称</td><td>主演</td><td>网站</td><td>导演</td><td>宣传词</td><td>关键词</td><td>简介</td><td>时常</td><td>类别</td><td>发行公司</td><td>发行日期</td><td>投票总数</td><td>投票均值</td><td>发行年份</td><td>预算（调整后）</td><td>票房（调整后）</td></tr>
# </tbody></table>
# 

# **请注意，你需要提交该报告导出的 `.html`、`.ipynb` 以及 `.py` 文件。**

# 
# 
# ---
# 
# ---
# 
# ## 第一节 数据的导入与处理
# 
# 在这一部分，你需要编写代码，使用 Pandas 读取数据，并进行预处理。

# 
# **任务1.1：** 导入库以及数据
# 
# 1. 载入需要的库 `NumPy`、`Pandas`、`matplotlib`、`seaborn`。
# 2. 利用 `Pandas` 库，读取 `tmdb-movies.csv` 中的数据，保存为 `movie_data`。
# 
# 提示：记得使用 notebook 中的魔法指令 `%matplotlib inline`，否则会导致你接下来无法打印出图像。

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

get_ipython().run_line_magic('matplotlib', 'inline')

movie_data = pd.read_csv('tmdb-movies.csv')


# ---
# 
# **任务1.2: ** 了解数据
# 
# 你会接触到各种各样的数据表，因此在读取之后，我们有必要通过一些简单的方法，来了解我们数据表是什么样子的。
# 
# 1. 获取数据表的行列，并打印。
# 2. 使用 `.head()`、`.tail()`、`.sample()` 方法，观察、了解数据表的情况。
# 3. 使用 `.dtypes` 属性，来查看各列数据的数据类型。
# 4. 使用 `isnull()` 配合 `.any()` 等方法，来查看各列是否存在空值。
# 5. 使用 `.describe()` 方法，看看数据表中数值型的数据是怎么分布的。
# 
# 

# In[6]:


print(movie_data.shape)


# In[7]:


movie_data.head(3)  # 查看前3行数据


# In[8]:


movie_data.tail(3)  # 查看后3行数据


# In[9]:


movie_data.sample(3)  # 随机选择3行数据查看


# In[10]:


movie_data.dtypes  ## 各列数据的数据类型


# In[11]:


movie_data.isnull().any()  ## 各列数据是否存在NaN


# In[12]:


movie_data.describe()  ## 查看各列数据的统计性描述


# ---
# 
# **任务1.3: ** 清理数据
# 
# 在真实的工作场景中，数据处理往往是最为费时费力的环节。但是幸运的是，我们提供给大家的 tmdb 数据集非常的「干净」，不需要大家做特别多的数据清洗以及处理工作。在这一步中，你的核心的工作主要是对数据表中的空值进行处理。你可以使用 `.fillna()` 来填补空值，当然也可以使用 `.dropna()` 来丢弃数据表中包含空值的某些行或者列。
# 
# 任务：使用适当的方法来清理空值，并将得到的数据保存。

# In[2]:


## 'imdb_id', 'director', 'genres', 'revenue'这4列会对后续的分析造成影响，如果有NaN值，则删除行
movie_data.dropna(axis=0, subset=['imdb_id', 'director', 'genres', 'revenue'], inplace=True)

## 将其它的NaN替换为'XXX'
movie_data.fillna('XXX', inplace=True)


# ---
# 
# ---
# 
# ## 第二节 根据指定要求读取数据
# 
# 
# 相比 Excel 等数据分析软件，Pandas 的一大特长在于，能够轻松地基于复杂的逻辑选择合适的数据。因此，如何根据指定的要求，从数据表当获取适当的数据，是使用 Pandas 中非常重要的技能，也是本节重点考察大家的内容。
# 
# 

# ---
# 
# **任务2.1: ** 简单读取
# 
# 1. 读取数据表中名为 `id`、`popularity`、`budget`、`runtime`、`vote_average` 列的数据。
# 2. 读取数据表中前1～20行以及48、49行的数据。
# 3. 读取数据表中第50～60行的 `popularity` 那一列的数据。
# 
# 要求：每一个语句只能用一行代码实现。

# In[59]:


## 数据表中名为 id、popularity、budget、runtime、vote_average 列的数据
data1 = movie_data[['id', 'popularity', 'budget', 'runtime', 'vote_average']]

## 数据表中前1～20行以及48、49行的数据
data2 = movie_data[1:21].append(movie_data[48:50])

## 数据表中第50～60行的 popularity 那一列的数据
data3 = movie_data[['popularity']][50:61]


# ---
# 
# **任务2.2: **逻辑读取（Logical Indexing）
# 
# 1. 读取数据表中 **`popularity` 大于5** 的所有数据。
# 2. 读取数据表中 **`popularity` 大于5** 的所有数据且**发行年份在1996年之后**的所有数据。
# 
# 提示：Pandas 中的逻辑运算符如 `&`、`|`，分别代表`且`以及`或`。
# 
# 要求：请使用 Logical Indexing实现。

# In[64]:


movie_popularity_greater_5 = movie_data[movie_data['popularity'] > 5]
movie_popularity_greater_5_release_year_after_1996 = movie_data[(movie_data['popularity'] > 5) & (movie_data['release_year'] > 1996)]


# ---
# 
# **任务2.3: **分组读取
# 
# 1. 对 `release_year` 进行分组，使用 [`.agg`](http://pandas.pydata.org/pandas-docs/version/0.22/generated/pandas.core.groupby.DataFrameGroupBy.agg.html) 获得 `revenue` 的均值。
# 2. 对 `director` 进行分组，使用 [`.agg`](http://pandas.pydata.org/pandas-docs/version/0.22/generated/pandas.core.groupby.DataFrameGroupBy.agg.html) 获得 `popularity` 的均值，从高到低排列。
# 
# 要求：使用 `Groupby` 命令实现。

# In[76]:


mean_revenue_groupby_release_year = movie_data.groupby(['release_year'])['revenue'].agg(['mean'])
mean_popularity_groupby_director = movie_data.groupby(['director'])['popularity'].agg(['mean']).sort_values(by=['mean'], ascending=False)


# ---
# 
# ---
# 
# ## 第三节 绘图与可视化
# 
# 接着你要尝试对你的数据进行图像的绘制以及可视化。这一节最重要的是，你能够选择合适的图像，对特定的可视化目标进行可视化。所谓可视化的目标，是你希望从可视化的过程中，观察到怎样的信息以及变化。例如，观察票房随着时间的变化、哪个导演最受欢迎等。
# 
# <table>
# <thead><tr><th>可视化的目标</th><th>可以使用的图像</th></tr></thead><tbody>
#  <tr><td>表示某一属性数据的分布</td><td>饼图、直方图、散点图</td></tr>
#  <tr><td>表示某一属性数据随着某一个变量变化</td><td>条形图、折线图、热力图</td></tr>
#  <tr><td>比较多个属性的数据之间的关系</td><td>散点图、小提琴图、堆积条形图、堆积折线图</td></tr>
# </tbody></table>
# 
# 在这个部分，你需要根据题目中问题，选择适当的可视化图像进行绘制，并进行相应的分析。对于选做题，他们具有一定的难度，你可以尝试挑战一下～

# **任务3.1：**对 `popularity` 最高的20名电影绘制其 `popularity` 值。

# In[171]:


## popularity最高的20名电影
max_20_popularity = movie_data.sort_values(by=['popularity'], ascending=False).head(20)
plt.scatter(data=max_20_popularity, x='original_title', y='popularity')
plt.xticks(rotation=90)
plt.xlabel('Movie Title')
plt.ylabel('Popularity')


# ---
# **任务3.2：**分析电影净利润（票房-成本）随着年份变化的情况，并简单进行分析。

# In[172]:


## 统计年份-电影净利润
movie_data['net_profit'] = movie_data['revenue_adj'] - movie_data['budget_adj']  ## 增加净利润列net_profit

# 每年总的电影净利润
totoal_net_profit_by_year = movie_data[['release_year', 'net_profit']].groupby(['release_year']).agg('sum')
plt.figure(figsize=(16, 18))
plt.subplot(211)
sb.pointplot(data=totoal_net_profit_by_year, x=totoal_net_profit_by_year.index, y='net_profit')
plt.xticks(rotation=60);
plt.xlabel("Release year")
plt.ylabel('Total net profit')

# 每年电影的平均净利润
average_net_profit_by_year = movie_data[['release_year', 'net_profit']].groupby(['release_year']).agg('mean')
plt.subplot(212)
sb.pointplot(data=average_net_profit_by_year, x=average_net_profit_by_year.index, y='net_profit');
plt.xticks(rotation=60);
plt.xlabel("Release year");
plt.ylabel('Average net profit');


# 分析：
# 1. 每年票房总的净利润随着年份的增长处于上涨状态。
# 2. 每年票房每部电影的平均经理如并没有随着年份的增长而上涨，在1977年达到峰值后，随后处于一个缓慢下滑的状态。
# 3. 每年票房总的净利润增长是由于每年上映的电影越来越多的原因。

# ---
# 
# **[选做]任务3.3：**选择最多产的10位导演（电影数量最多的），绘制他们排行前3的三部电影的票房情况，并简要进行分析。

# In[169]:


## 电影数量最多的10位导演的名称
names = movie_data['director'].value_counts().iloc[0:10].index.values

## 前10多产导演的数据
ten_directors_by_movie_count = movie_data[movie_data['director'].isin(names)]

## 取出每个导演票房最高的3部电影
ten_directors_by_movie_count = ten_directors_by_movie_count.groupby(['director']).apply(lambda x: x.sort_values('revenue_adj', ascending=False).head(3))

plt.figure(figsize=(20, 30))

##
for i in range(10):
    plt.subplot(4, 3, i + 1)
    tmp = ten_directors_by_movie_count.iloc[(i * 3):(i + 1) * 3, :]
    sb.pointplot(data=tmp, x='budget_adj', y='revenue_adj');
    plt.title(tmp['director'][0], loc='center')
    plt.xlabel('Budget Adjust')
    plt.ylabel('Revenue Adjust')


# In[ ]:


分析：从上面10张图可以看出，有7位导演的预算和票房并不成正比


# ---
# 
# **[选做]任务3.4：**分析1968年~2015年六月电影的数量的变化。

# In[130]:


## 选取1968-2015年六月电影数据
movie_June = movie_data[(movie_data['release_year'] >= 1968) & (movie_data['release_year'] <= 2015) & (movie_data['release_date'].str.startswith('6'))].copy()

## 统计1968-2015年电影数量
movie_June_count = movie_June[['release_year']].groupby(['release_year'])['release_year'].agg(['count'])
plt.figure(figsize=(16, 9))
sb.pointplot(data=movie_June_count, x=movie_June_count.index, y='count');
plt.xticks(rotation=90);
plt.xlabel('Release year');
plt.ylabel('Movie count');


# 分析：由上图可以看出，1968-2015年六月电影数量呈逐年上升趋势

# ---
# 
# **[选做]任务3.5：**分析1968年~2015年六月电影 `Comedy` 和 `Drama` 两类电影的数量的变化。

# In[164]:


## Comedy电影
comedy_data = movie_June[movie_June['genres'].str.contains('Comedy')]
comedy_data_count = comedy_data.groupby(['release_year'])['release_year'].agg(['count'])

## 有些年份在六月没有Comedy电影
zeros_data = pd.DataFrame(np.zeros(2015 - 1968 + 1, dtype='int64'), index=np.arange(1968, 2016, 1), columns=['count'])
comedy_data_count = zeros_data.add(comedy_data_count, fill_value=0).astype(int)

## drama电影
drama_data = movie_June[movie_June['genres'].str.contains('Drama')]
drama_data_count = drama_data.groupby(['release_year'])['release_year'].agg(['count'])
plt.figure(figsize=(16, 9))
y_ticks = np.arange(0, max(comedy_data_count['count'].max(), drama_data_count['count'].max()) + 1, 1)
sb.pointplot(data=comedy_data_count, x=comedy_data_count.index, y='count');
sb.pointplot(data=drama_data_count, x=drama_data_count.index, y='count', color='red');  ## 红色表示Drama电影
plt.xticks(rotation=90)
plt.yticks(y_ticks);
plt.xlabel('Release year');
plt.ylabel('Movie count');


# 分析：从上图数据可以看出，在六月电影中，Comedy和Drama数量变化趋势比较接近

# > 注意: 当你写完了所有的代码，并且回答了所有的问题。你就可以把你的 iPython Notebook 导出成 HTML 文件。你可以在菜单栏，这样导出**File -> Download as -> HTML (.html)、Python (.py)** 把导出的 HTML、python文件 和这个 iPython notebook 一起提交给审阅者。
