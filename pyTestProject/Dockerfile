FROM python
WORKDIR pyTestProject/tests
COPY requirements.txt .
COPY . .
RUN pip install -r requirements.txt
CMD python -m pytest -s -v


