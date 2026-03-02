FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

ENV TZ="Asia/Seoul"
RUN date

WORKDIR /app/

COPY ./requirements.txt /app/
RUN pip3 install -r requirements.txt

COPY ./main.py /app/main.py

EXPOSE 8000

CMD ["python", "main.py"]