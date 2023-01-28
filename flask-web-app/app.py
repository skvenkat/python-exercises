from flask import Flask

app = Flask(__name__)
env_config = os.getenv("APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)

@app.route("/")
def index():
    is_dev_env = app.config.get("DEVELOPMENT")
    is_staging_env = app.config("DEBUG")
    
    if is_dev_env and is_staging_env:
        deployment_env = "DEV Environment"
    elif is is_staging_env:
        deployment_env = "STAGING Environment"
    else:
        deployment_env = "PRODUCTION Environment"

    return f"The app has been deployed in {deployment_env}!!!"
