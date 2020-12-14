FROM python:3.7
ENV STRINGS=ab,ab,abc
ARG queries
ADD main.py /
ADD SparseArray.py /
RUN pip install flask
ENTRYPOINT [ "python", "./main.py" ]