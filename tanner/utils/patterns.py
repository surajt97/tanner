import re

INDEX = re.compile('(/index.html|/)')
RFI_ATTACK = re.compile('.*((http(s){0,1}|ftp(s){0,1}):).*', re.IGNORECASE)
SQLI_ATTACK = re.compile('.*(select|drop|update|union|insert|alter|declare|cast)( |\().*', re.IGNORECASE)
LFI_ATTACK = re.compile('.*(\/\.\.)*(home|proc|usr|etc)\/.*')
LFI_FILEPATH = re.compile('((\.\.|\/).*)')
XSS_ATTACK = re.compile('.*<(.|\n)*?>')
CMD_ATTACK = re.compile('.*(alias|cat|cd|cp|echo|exec|find|for|grep|ifconfig|ls|man|mkdir|netstat|ping|ps|pwd|uname|wget|touch|while).*')
REMOTE_FILE_URL = re.compile('(.*(http(s){0,1}|ftp(s){0,1}):.*)')
WORD_PRESS_CONTENT = re.compile('\/wp-content\/.*')
HTML_TAGS = re.compile('.*<(.*)>.*')
QUERY = re.compile('.*\?.*=')