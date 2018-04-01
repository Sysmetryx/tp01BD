from google.cloud import bigquery


def myQuerry():
    client = bigquery.Client()
    query_job = client.query("""
SELECT
            COUNT(born_dead)
        FROM
            'bigquerry-public-data:samples.natality'
        WHERE
            (alcohol_use == TRUE and born_dead == TRUE)""");

    results = query_job.result()  # Waits for job to complete.

    for row in results:
        print("{} : {} views".format(row.url, row.view_count))


if __name__ == '__main__':
    myQuerry()