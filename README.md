# Spotify ETL using Python and AWS

This project involves developing an ETL (Extract, Transform, Load) pipeline using Python and AWS services to obtain artist, album, and song information from the "Top 200 Global" playlist on Spotify. This playlist is updated daily and consists of the top 200 songs streamed globally.

## Objective

The objective of this project is to build a fully automated data pipeline that extracts data from the Spotify API, transforms it for analysis, and loads the transformed data into Amazon S3. The data is then queried using Amazon Athena, with AWS Glue managing cataloging and metadata.

## Architecture Overview

The architecture of this project includes the following components:

- **Search**
- **Write**
- **Sign Up**
- **Sign In**

Below is an overview of the tools and services used in the project:

- **S3 (Simple Storage Service):** Used to store raw and transformed data.
- **Lambda:** Serverless compute service used to run Python code for data extraction and transformation.
- **CloudWatch:** Monitors and logs AWS resources and sets alarms.
- **EventBridge:** Schedules and triggers events to automate data extraction.
- **Glue Data Catalog:** Manages metadata and acts as a central repository for storing and organizing data schemas.
- **Athena:** Performs interactive queries on data stored in S3 using SQL.

## ETL Process Overview

### 1. Extract
- Data is extracted from the Spotify API using the Spotipy library.
- The extraction code is deployed using AWS Lambda.
- A trigger in EventBridge automates the data extraction every day at 4 PM UTC.
- The extracted data is saved in the `top_200_global/raw_data/to_process` folder in the S3 bucket.

### 2. Transform
- A trigger on S3 detects when new data is added to the `top_200_global/raw_data/to_process` folder, invoking the transformation code on Lambda.
- The transformation code cleans and prepares the data, creating separate files for albums, artists, and songs.
- The transformed data is stored in the respective subfolders in `top_200_global/transformed_data`.

### 3. Load
- AWS Glue's crawler infers the schema when new data arrives in the transformed data folders.
- The Glue Data Catalog manages metadata, which can be queried using Athena.

## Data Model

The data model is designed to store and process the following:
- **Album Data**
- **Artist Data**
- **Song Data**

Each dataset is stored in separate folders in the S3 bucket and is accessible for querying via Athena.


## Conclusion

This project serves as a comprehensive introduction to building ETL pipelines using Python and AWS. By working with the Spotify API and core AWS services, you gain hands-on experience in setting up a scalable and automated data processing system.
