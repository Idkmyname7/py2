import re
import datetime
from models import db, AccessLog


def parse_file(log_file):
    pattern = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[(.*)\] "(\w+) (.+) HTTP/[\d\.]+" (\d+) (\d+)'
    with open(log_file) as f:
        for line in f:
            match = re.match(pattern, line)
            if match:
                ip, date_str, method, url, status, size = match.groups()
                date = datetime.datetime.strptime(date_str, '%d/%b/%Y:%H:%M:%S %z')
                access_log = AccessLog(ip=ip, date=date, method=method, url=url, status=status, size=size)
                db.session.add(access_log)
        db.session.commit()