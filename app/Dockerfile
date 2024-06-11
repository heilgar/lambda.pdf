FROM public.ecr.aws/lambda/python:3.10

RUN yum update && \
    yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm && \
    yum -y install ghostscript python3-tk mesa-libGL python3-opencv && \
    yum clean all

COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR ${LAMBDA_TASK_ROOT}

COPY app.py ${LAMBDA_TASK_ROOT}
COPY sample.pdf /tmp/sample.pdf

CMD ["app.handler"]
