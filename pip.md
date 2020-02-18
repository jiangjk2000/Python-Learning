## pip更新所有packages
### cmd实现
```cmd
pip list --outdated --format=legacy |awk '{print $1}' |xargs sudo -H pip install -U
```
这条应该是cmd的命令.
### python实现
```python
import pip
from subprocess import call
for package in pip.get_installed_distributions():
   call('pip install --upgrade' + package.project_name)
```
### PowerShell
```shell
pip freeze > requirements.txt
```
再通过正则替换,将(==版本号)去掉.
```re
==.*
```
最后
```shell
pip install -r requirements.txt --upgrade
```