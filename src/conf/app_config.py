import os

def app_config(app):
    app.config.from_object('src.conf.flask_api_conf')
    if os.environ.get('FLASK_API_CONF') is not None:
        app.config.from_envvar('FLASK_API_CONF')

    sqlalchemy_database_uri_str = os.environ.get('FLASK_API_SQLALCHEMY_DATABASE_URI')
    if sqlalchemy_database_uri_str is not None:
        app.config['SQLALCHEMY_DATABASE_URI'] = sqlalchemy_database_uri_str

    init_sample_data_str = os.environ.get('FLASK_API_INIT_SAMPLE_DATA')
    if init_sample_data_str is not None:
        app.config['INIT_SAMPLE_DATA'] = eval(init_sample_data_str)

    cleanup_invalidated_tokens_interval_seconds_str = os.environ.get('FLASK_API_CLEANUP_INVALIDATED_TOKENS_INTERVAL_SECONDS')
    if cleanup_invalidated_tokens_interval_seconds_str is not None:
        app.config['CLEANUP_INVALIDATED_TOKENS_INTERVAL_SECONDS'] = eval(cleanup_invalidated_tokens_interval_seconds_str)

    return app
