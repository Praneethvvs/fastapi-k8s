FROM python:3.9
COPY . /usr/app
WORKDIR /usr/app
RUN chmod +x ./start.sh
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["./start.sh"]