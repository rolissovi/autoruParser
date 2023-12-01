FROM python
WORKDIR /bin/data-analytics
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY data_analytics.py /bin/data-analytics
ENTRYPOINT [ "python", "data_analytics.py"]