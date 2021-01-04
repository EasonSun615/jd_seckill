import re
import datetime
import os


def alter(file_name):
    # 2021-01-04 09:59:59.900
    regex = re.compile('2021-(\d{2})-(\d{2})')
    with open(file_name, 'r') as f1, open("%s.bak" % file_name, 'w') as f2:
        for line in f1:
            rst = regex.search(line)
            if rst != None:
                tomorrow = datetime.date.today() + datetime.timedelta(days=1)
                line = re.sub(regex, tomorrow.isoformat(), line)
            f2.write(line)
        os.remove(file_name)
        os.rename("%s.bak"%file_name, file_name)


if __name__ == "__main__":
    file_name = "./config.ini"
    alter(file_name)