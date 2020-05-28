# Django Settings
DEBUG="True"  # Django后台是否以debug模式运行, 可选True/False
ALLOWED_HOSTS="*,127.0.0.1,localhost"  # 配置Django Allowed_Hosts, 如果DEBUG为False, 需要将访问的host地址添加进来，如'localhost,github.vipkid.com.cn'

# Database Settings
# DATABASE choice is mysql or sqlite
DATABASE="sqlite"  # 数据库类型, 可选sqlite或mysql
DB_NAME="github"  # 数据库名称
DB_HOST="127.0.0.1"  # mysql host
DB_PORT="3306"  # mysql port
DB_USER="root"  # mysql用户名
DB_PASSWORD="vipkid@2018"  # mysql密码

# Redis Settings
REDIS_HOST="127.0.0.1"  # redis host
REDIS_PORT="6379"  # redis port
REDIS_PASSWORD=""  # redis password

# Email Settings
# If you do not fill it in, it is None/False
EMAIL_HOST="smtp.139.com"  # smtp host
EMAIL_PORT="25"  # smtp port
FROM_EMAIL="13862292780@139.com"  # 发件人
EMAIL_HOST_USER="security@example.com"  # email user, 如为匿名发送，将值设为空字符即可
EMAIL_HOST_PASSWORD="password123!@#"  # email password, 如为匿名发送，将值设为空字符即可
EMAIL_USE_TLS="False"  # 与SMTP服务器通信时是否使用TLS（安全）连接, 可选True/False
EMAIL_USE_SSL="False"  # 与SMTP服务器通信时是否使用SSL（安全）连接, 可选True/False

