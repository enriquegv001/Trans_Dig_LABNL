FROM python:3.10

WORKDIR /src

ADD ./ /src

#COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000 

#COPY . .

#CMD ["python", "api.py"]
#CMD ["uvicorn", "main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]
CMD ["uvicorn", "api.py", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]
