from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+pymysql://root:123456@47.102.218.113:3306/edu?charset=utf8')

# 生成数据库连接类
DbSession = sessionmaker(bind=engine)

# 创建会话对象
session = DbSession()

# 生成所有模型类的基类
Base = declarative_base(bind=engine)