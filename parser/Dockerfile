FROM python
WORKDIR /src/parser
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY parser.py /src/parser
ENTRYPOINT [ "python", "parser.py"]