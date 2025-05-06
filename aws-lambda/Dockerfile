FROM public.ecr.aws/lambda/python:3.12

COPY . ${LAMBDA_TASK_ROOT}
RUN pip install -e .

COPY lambda_function.py ${LAMBDA_TASK_ROOT}
CMD [ "lambda_function.handler" ]
