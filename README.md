<h1>Comparative Analysis of Data Orchestration Frameworks</h1>

<h2>Project Overview</h2>

<p>
This project presents a <strong>hands-on comparison</strong> of three data orchestration frameworks:
</p>

<ul>
    <li><strong>Apache Airflow</strong></li>
    <li><strong>Prefect</strong></li>
    <li><strong>Dagster</strong></li>
</ul>

<p>
The <strong>same ETL pipeline</strong> is implemented using all three tools to evaluate differences in:
</p>

<ul>
    <li>Developer experience</li>
    <li>Core abstractions</li>
    <li>Retry and backfill mechanisms</li>
    <li>Setup complexity</li>
    <li>Observability and UI</li>
    <li>Output parity</li>
</ul>

<div class="success">
    All pipelines process identical synthetic user activity data and produce
    <strong>bit-for-bit identical Parquet outputs</strong>.
</div>

<h2>Repository Structure</h2>

<pre>
gpp-data-orchestration/
│
├── airflow/                 # Apache Airflow implementation
│   ├── dags/
│   ├── docker-compose.yml
│   ├── Dockerfile
│   └── README.html
│
├── prefect/                 # Prefect implementation
│   ├── prefect_flow.py
│   └── README.html
│
├── dagster/                 # Dagster implementation
│   ├── dagster_job.py
│   └── README.html
│
├── shared/                  # Shared ETL business logic
│   └── etl_logic.py
│
├── data/                    # Input and output data
│   ├── user_events.csv
│   ├── airflow_output.parquet
│   ├── prefect_output.parquet
│   ├── dagster_output.parquet
│
├── COMPARISON.md             # Detailed framework comparison
└── README.html               # This file
</pre>

<h2>Shared ETL Pipeline Logic</h2>

<p>
The core business logic is implemented <strong>once</strong> and reused across all orchestration
frameworks. This guarantees that behavioral differences arise from the orchestrators themselves,
not duplicated or inconsistent transformation logic.
</p>

<h3>Extract</h3>
<ul>
    <li>Reads a CSV file containing user activity events</li>
</ul>

<h3>Transform</h3>
<ul>
    <li>Filters out events from excluded countries</li>
    <li>Calculates session duration per user</li>
    <li>Aggregates total events per user per day</li>
    <li>Introduces controlled intermittent failure to test retry behavior</li>
</ul>

<h3>Load</h3>
<ul>
    <li>Writes aggregated results to a Parquet file</li>
</ul>

<div class="highlight">
    The ETL logic lives in <code>shared/etl_logic.py</code> and is imported by Airflow,
    Prefect, and Dagster implementations without modification.
</div>

<h2>Prerequisites</h2>

<ul>
    <li>Windows / Linux / macOS</li>
    <li>Python <strong>3.10</strong></li>
    <li>Git</li>
    <li>Docker & Docker Compose (required for Airflow)</li>
</ul>

<h2>How to Run Each Pipeline</h2>

<p>
Each orchestration framework has its own setup and execution instructions.
Follow the framework-specific guides:
</p>

<ul>
    <li>
        <strong>Airflow:</strong>
        <a href="airflow/README.md">Setup & Execution Guide</a>
    </li>
    <li>
        <strong>Prefect:</strong>
        <a href="prefect/README.md">Setup & Execution Guide</a>
    </li>
    <li>
        <strong>Dagster:</strong>
        <a href="dagster/README.md">Setup & Execution Guide</a>
    </li>
</ul>

<h2>Output Parity Verification</h2>

<p>
All three pipelines generate identical Parquet outputs.
Example parity check:
</p>

<pre>
python -c "
import pandas as pd

print(
    pd.read_parquet('data/airflow_output.parquet')
      .equals(pd.read_parquet('data/prefect_output.parquet'))
)
"
</pre>

<h2>Comparative Analysis</h2>

<p>
A detailed, evidence-based comparison is provided in:
</p>

<p>
<strong>
<a href="COMPARISON.md">📄 COMPARISON.md</a></strong>
</p>

<p>
This includes:
</p>

<ul>
    <li>Developer experience comparison</li>
    <li>Retry and backfill implementation differences</li>
    <li>UI and observability analysis</li>
    <li>Final recommendations</li>
</ul>

<h2>Conclusion</h2>

<p>
This project demonstrates how different data orchestration frameworks approach the
<strong>same data engineering problem</strong> and highlights the trade-offs involved
in choosing the right tool for different use cases.
</p>

<p>
The results show that orchestration choice is less about raw capability and more about
<strong>team workflow</strong>, <strong>infrastructure maturity</strong>,
and <strong>development ergonomics</strong>.
</p>

</body>
</html>
