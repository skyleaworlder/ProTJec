FROM python:3.7

WORKDIR /home/website/ProTJec/back_end

COPY . .
RUN pip install -r requirements.txt && pip install .

CMD ["gunicorn", "ProTJec_backend:app", "-c", "./gunicorn.conf.py"]
