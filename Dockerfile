FROM python:3-alpine

RUN apk add --no-cache git
RUN git clone https://github.com/um-computacion-tm/ajedrez-2024-mmruvinsky.git

WORKDIR /ajedrez-2024-mmruvinsky

RUN pip install -r requirements.txt

CMD ["sh", "-c", "coverage run -m unittest && coverage report -m && python main.py"]

# docker buildx build -t ajedrez-2024-mmruvinsky .
# docker run -i ajedrez-2024-mmruvinsky
