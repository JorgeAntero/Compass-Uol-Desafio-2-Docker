FROM python:3.9-slim
RUN adduser --system --group --no-create-home --disabled-login jorge
WORKDIR /app 
RUN chown -R jorge:jorge /app
COPY requirements.txt . 
RUN pip install -r requirements.txt 
USER jorge
COPY . . 
CMD ["python", "app.py"]