FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update

RUN apt-get install ffmpeg libsm6 libxext6  -y \
    && apt-get install -y --no-install-recommends \
    build-essential \
    python3.9 \
    python3-pip \
    python3-venv \
    python3-dev \
    && rm -rf /var/cache/apt/archives \
    && rm -rf /var/lib/apt/lists

RUN python3.9 -m pip install --upgrade pip

COPY ./ /

RUN pip3 install -r requirements_prod.txt

WORKDIR /demo

EXPOSE 8501

ENTRYPOINT ["streamlit", "run"]
CMD ["web_demo.py"]
