from sqlalchemy import create_engine
db_connection_string = "mysql+pymysql://b0ohtjsnkblon805jnyp:pscale_pw_Gk9sKOg2kwB0wv1D0fuYeekUsnxthWepvxDOweCK2xE@aws.connect.psdb.cloud/gtmenterprise?charset=utf8mb4"
engine = create_engine(
  db_connection_string,
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  }
)
