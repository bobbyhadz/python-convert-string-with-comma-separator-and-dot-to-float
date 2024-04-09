# Python: Convert string with comma separator and dot to float

import locale


# ✅ Convert string with comma separator and dot to float (locale.atof())
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

my_str = '456,789.4567'

result = locale.atof(my_str)
print(result)  # 👉️ 456789.4567