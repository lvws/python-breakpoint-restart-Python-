# python-breakpoint-restart-Python-
让中断的任务，可以跳过已分析的部分继续向前

## 安装
pip install Brestart (python2)     
pip install Brestart2 (python3)

## 方法
brestart.preRunCheck()
在脚本运行的开始阶段检查脚本所在目录是否存在中断文件（pkl 保存 .\_\_name\_\_.pkl）；若存在这一文件，就解析文件内容，读取阶段性的运行结果。
在工作脚本中特别用@brestart.logFunc 装饰的Function，在运行结束后会被记录运行以及运行的结果；
brestart.end()
在工作脚本正常运行结束后，会将暂存的pkl文件清除，不影响下一次的分析。

注： 如果，是输入参数引起的错误中断，可以手动删除.\_\_name\_\_.pkl 文件，使其可以重头开始运行。
