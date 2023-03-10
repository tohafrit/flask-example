FROM python

WORKDIR /workspace

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y netcat

RUN pip install --upgrade pip
COPY ./requirements.txt /workspace/
RUN pip install -r requirements.txt

COPY ./simple_server.py /workspace/
COPY ./logs /workspace/

# CMD ["python", "simple_server.py"]