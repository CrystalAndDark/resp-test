import yaml
import os

# 获取当前脚本所在文件夹路径
curPath = os.path.dirname(os.path.realpath(__file__))
# 获取yaml文件路径
yamlPath = os.path.join(curPath, "test.yaml")

# open方法打开直接读出来
f = open(yamlPath, 'r', encoding='utf-8')
cfg = f.read()
print(type(cfg))  # 读出来是字符串
print(cfg)

d = yaml.load(cfg, Loader=yaml.FullLoader)  # 用load方法转字典
print(d)
print(type(d))

required_params = d['required']
for param in required_params:
    pr_results = param['pr_job_result']
    for i in pr_results:
        print(pr_results[i])
        # file_path = "/job_data/" + pr_results[i]
        file_path = pr_results[i]
        file = open(file_path, "w")
        file.write("hello world")
