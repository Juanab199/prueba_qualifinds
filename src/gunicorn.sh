gunicorn --workers 1 --worker-class uvicorn.workers.UvicornWorker --access-logfile - --error-logfile - --bind 0.0.0.0:8080 app.main:app