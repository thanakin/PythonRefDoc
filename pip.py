'''

print('Check if PIP is Installed')

pip --version

pip install camelcase

import camelcase
c = camelcase.CamelCase()
txt = "hello world"
print(c.hump(txt))


pip uninstall camelcase

pip list
'''