FROM python:3.8.5

# Update and install system packages
RUN apt-get update -y && \
  apt-get install --no-install-recommends -y -q \
  git libpq-dev python-dev && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install DBT
RUN pip install -U pip
RUN python -m pip install dbt-postgres

# Download DBT_parse_package 
RUN pip install dbt_log_parser==0.2.1

RUN mkdir dbt

WORKDIR dbt

COPY profiles.yml .

# Set environment variables 
ENV DBT_DIR /dbt

# Set working directory
WORKDIR $DBT_DIR

COPY . .

RUN dbt deps

WORKDIR /