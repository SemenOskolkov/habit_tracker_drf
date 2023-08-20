FROM python:3

WORKDIR /habit_tracker_drf

COPY ./requirements.txt /habit_tracker_drf

RUN pip install --upgrade pip
RUN pip install -r /habit_tracker_drf/requirements.txt

COPY . .
