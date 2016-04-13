FROM pypy:2
#FROM python:3.4
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
#CMD python app.py
CMD /usr/local/bin/gunicorn app:app --bind 0.0.0.0:6000 --log-level=debug --access-logfile - --error-logfile - --timeout 300 --workers 4 --max-requests 10000 --user nobody --group nogroup --chdir /code
