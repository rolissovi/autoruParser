FROM python
WORKDIR /src/data-analytics
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY data_analytics.py /src/data-analytics
ENTRYPOINT [ "python", "data_analytics.py"]