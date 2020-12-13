FROM python:3.7
ENV STRINGS=ab,ab,abc
ARG queries
ADD main.py /
ADD SparseArray.py /
ENTRYPOINT [ "python", "./main.py" ]