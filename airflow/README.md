<h1>Apache Airflow Implementation</h1>



<h2>Overview</h2>

<p>

This directory contains the <strong>Apache Airflow</strong> implementation of the shared ETL pipeline.

Airflow is used strictly as an <strong>orchestration layer</strong> to coordinate extract,

transform, and load tasks via a DAG.

</p>



<p>

All business logic is imported from the shared ETL module.

Airflow does not perform data transformation itself.

</p>



<h2>Prerequisites</h2>

<ul>

&nbsp;   <li>Docker</li>

&nbsp;   <li>Docker Compose</li>

</ul>



<h2>Setup Instructions</h2>



<p>From the <code>airflow/</code> directory:</p>



<pre>

docker compose build --no-cache

docker compose up

</pre>



<p>

Once the services are running, open:

</p>



<pre>

http://localhost:8080

</pre>



<h3>Login Credentials</h3>

<ul>

&nbsp;   <li>Username: <code>admin</code></li>

&nbsp;   <li>Password: <code>admin</code></li>

</ul>



<h2>DAG Details</h2>



<ul>

&nbsp;   <li><strong>DAG ID:</strong> <code>user\_activity\_etl</code></li>

</ul>



<h3>Tasks</h3>

<ul>

&nbsp;   <li><code>extract\_data</code></li>

&nbsp;   <li><code>transform\_data</code> (configured with retries)</li>

&nbsp;   <li><code>load\_data</code></li>

</ul>



<h3>Retry Policy</h3>

<ul>

&nbsp;   <li>Retries: <strong>2</strong></li>

&nbsp;   <li>Retry Delay: <strong>10 seconds</strong></li>

</ul>



<h3>Executor</h3>

<ul>

&nbsp;   <li><strong>LocalExecutor</strong></li>

</ul>



<div class="highlight">

Airflow retries are task-level and state-driven.

Failures persist until task state is explicitly cleared.

</div>



<h2>Running the Pipeline</h2>



<ol>

&nbsp;   <li>Enable the DAG in the Airflow UI</li>

&nbsp;   <li>Trigger the DAG manually</li>

&nbsp;   <li>Monitor execution using the Graph View and task logs</li>

</ol>



<h3>Output File</h3>

<pre>

data/airflow\_output.parquet

</pre>



<h2>Backfill Execution</h2>



<p>

Backfills must be triggered explicitly via the CLI:

</p>



<pre>

docker compose exec airflow-webserver \\

airflow dags backfill user\_activity\_etl \\

--start-date 2026-01-01 \\

--end-date 2026-01-01

</pre>



<h2>Notes and Limitations</h2>



<div class="warning">

<ul>

&nbsp;   <li>Airflow does <strong>not</strong> support in-memory data passing between tasks</li>

&nbsp;   <li>Intermediate results are written to disk</li>

&nbsp;   <li>Task state must be manually cleared when re-running failed tasks</li>

</ul>

</div>



<h2>Design Intent</h2>

<p>

This implementation intentionally uses Airflow in its traditional role:

<strong>reliable orchestration with explicit state management</strong>.

</p>



<p>

The goal is to evaluate Airflow’s strengths and weaknesses when compared

to Prefect and Dagster using the same ETL logic and output constraints.

</p>



