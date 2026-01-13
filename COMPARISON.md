<h1>Comparative Analysis of Data Orchestration Frameworks</h1>

<p>
This project presents a <strong>hands-on comparative analysis</strong> of three widely used
data orchestration frameworks: <strong>Apache Airflow</strong>, <strong>Prefect</strong>,
and <strong>Dagster</strong>.
</p>

<p>
Rather than a feature checklist, the comparison is based on implementing the
<strong>same ETL pipeline</strong> in all three systems and evaluating real-world behavior:
developer experience, retries, backfills, UI, and setup complexity.
</p>

<div class="highlight">
This document reflects <strong>actual implementation pain</strong>, debugging effort,
and execution behavior observed during development — not marketing claims.
</div>

<h2>Pipeline Description</h2>

<h3>Input Data</h3>
<ul>
    <li>CSV file containing synthetic user activity data</li>
    <li>Columns: <code>user_id</code>, <code>event_type</code>, <code>timestamp</code>, <code>country</code></li>
</ul>

<h3>Transformations</h3>
<ol>
    <li>Filter out events from excluded countries (e.g., US)</li>
    <li>Calculate session duration per user (first event to last event)</li>
    <li>Aggregate total number of events per user per day</li>
    <li>Introduce controlled intermittent failure to test retry behavior</li>
</ol>

<h3>Output</h3>
<ul>
    <li>Parquet file</li>
    <li>Identical schema and content across all frameworks</li>
    <li>Output parity verified using Pandas equality checks</li>
</ul>

<h3>Parity Requirement</h3>
<div class="success">
For the same input and parameters, all three orchestrators produce
<strong>bit-for-bit identical Parquet outputs</strong>.
</div>

<h2>Apache Airflow</h2>

<h3>Developer Experience</h3>
<p>
Airflow has the <strong>steepest learning curve</strong>. Writing the DAG is not difficult,
but the surrounding infrastructure (Docker, metadata DB, scheduler, webserver, task state)
significantly slows development and debugging.
</p>

<p>
Small mistakes — missing parameters, stale task state, failed imports —
often cause repeated failures that are non-obvious to beginners.
</p>

<h3>Core Concepts</h3>
<ul>
    <li>DAGs</li>
    <li>Operators</li>
    <li>Tasks</li>
    <li>XCom (metadata passing, not data passing)</li>
</ul>

<h3>Retries and Backfills</h3>
<ul>
    <li>Retries are configurable per task and work reliably</li>
    <li>Backfills must be explicitly triggered via CLI</li>
    <li>Task state must be manually cleared to recover from failures</li>
</ul>

<h3>UI and Observability</h3>
<ul>
    <li>Most mature UI among the three</li>
    <li>Excellent DAG visualization and task logs</li>
    <li>UI behavior tightly coupled to task state, which can confuse beginners</li>
</ul>

<h3>Setup Complexity</h3>
<ul>
    <li>Requires Docker, Postgres, scheduler, and webserver</li>
    <li>Custom Docker images required for dependencies (e.g., pyarrow)</li>
    <li>Most complex local setup</li>
</ul>

<h3>Pros</h3>
<ul>
    <li>Industry standard</li>
    <li>Very mature ecosystem</li>
    <li>Strong scheduling and backfill support</li>
</ul>

<h3>Cons</h3>
<div class="warning">
<ul>
    <li>Heavy setup and maintenance overhead</li>
    <li>Poor local iteration speed</li>
    <li>Data passing via XCom is impractical</li>
    <li>State management can be frustrating</li>
</ul>
</div>

<h2>Prefect</h2>

<h3>Developer Experience</h3>
<p>
Prefect provides the <strong>smoothest and fastest developer experience</strong>.
Pipelines feel like normal Python programs, making local development and debugging trivial.
</p>

<p>
Once the correct version (Prefect 2.x) and environment were configured,
development was dramatically easier than Airflow.
</p>

<h3>Core Concepts</h3>
<ul>
    <li>Flows</li>
    <li>Tasks</li>
    <li>Python-first execution model</li>
</ul>

<h3>Retries and Parameterization</h3>
<ul>
    <li>Retries declared directly on tasks</li>
    <li>Clean and readable retry logic</li>
    <li>Parameters passed naturally via function arguments</li>
</ul>

<h3>UI and Observability</h3>
<ul>
    <li>Lightweight UI</li>
    <li>Less feature-rich than Airflow</li>
    <li>Sufficient for execution monitoring</li>
</ul>

<h3>Setup Complexity</h3>
<ul>
    <li>Very low</li>
    <li>No database or scheduler required locally</li>
    <li>Python virtual environment is sufficient</li>
</ul>

<h3>Pros</h3>
<ul>
    <li>Excellent local development experience</li>
    <li>In-memory data passing</li>
    <li>Minimal boilerplate</li>
    <li>Fast iteration</li>
</ul>

<h3>Cons</h3>
<div class="warning">
<ul>
    <li>Versioning pitfalls (Prefect 2 vs Prefect 3)</li>
    <li>UI less mature than Airflow</li>
    <li>Requires strict version pinning discipline</li>
</ul>
</div>

<h2>Dagster</h2>

<h3>Developer Experience</h3>
<p>
Dagster sits between Airflow and Prefect.
It is more structured than Prefect but far less painful than Airflow.
</p>

<h3>Core Concepts</h3>
<ul>
    <li>Ops</li>
    <li>Jobs</li>
    <li>Explicit execution model</li>
</ul>

<h3>Retries and Execution Model</h3>
<ul>
    <li>Retry policies explicitly defined on ops</li>
    <li>Jobs must be explicitly executed</li>
    <li>Clear separation between definition and execution</li>
</ul>

<h3>UI and Observability</h3>
<ul>
    <li>Clean, modern UI</li>
    <li>Excellent graph visualization</li>
    <li>Logs and retries easy to follow</li>
</ul>

<h3>Setup Complexity</h3>
<ul>
    <li>Moderate</li>
    <li>No mandatory Docker for local development</li>
    <li>Requires understanding Dagster abstractions</li>
</ul>

<h3>Pros</h3>
<ul>
    <li>Explicit and predictable behavior</li>
    <li>Strong structure for larger pipelines</li>
    <li>Better local development than Airflow</li>
</ul>

<h3>Cons</h3>
<div class="warning">
<ul>
    <li>More boilerplate than Prefect</li>
    <li>Explicit execution required</li>
    <li>Slightly higher learning curve than Prefect</li>
</ul>
</div>

<h2>Side-by-Side Comparison</h2>

<table>
    <tr>
        <th>Aspect</th>
        <th>Airflow</th>
        <th>Prefect</th>
        <th>Dagster</th>
    </tr>
    <tr>
        <td>Setup Effort</td>
        <td>Very High</td>
        <td>Low</td>
        <td>Medium</td>
    </tr>
    <tr>
        <td>Local Development</td>
        <td>Poor</td>
        <td>Excellent</td>
        <td>Good</td>
    </tr>
    <tr>
        <td>Data Passing</td>
        <td>Files / XCom</td>
        <td>In-memory</td>
        <td>In-memory</td>
    </tr>
    <tr>
        <td>Retry Handling</td>
        <td>Verbose</td>
        <td>Clean</td>
        <td>Explicit</td>
    </tr>
    <tr>
        <td>UI Experience</td>
        <td>Mature</td>
        <td>Lightweight</td>
        <td>Structured</td>
    </tr>
    <tr>
        <td>Learning Curve</td>
        <td>Steep</td>
        <td>Gentle</td>
        <td>Moderate</td>
    </tr>
    <tr>
        <td>Best Use Case</td>
        <td>Enterprise scheduling</td>
        <td>Rapid pipelines</td>
        <td>Structured data apps</td>
    </tr>
</table>

<h2>Final Recommendation</h2>

<ul>
    <li><strong>Use Apache Airflow</strong> when you need complex scheduling, historical backfills,
        and have mature infrastructure support.</li>
    <li><strong>Use Prefect</strong> when rapid development, Python-centric pipelines,
        and fast iteration are priorities.</li>
    <li><strong>Use Dagster</strong> when structure, correctness, and maintainability matter
        without Airflow’s operational overhead.</li>
</ul>

<h2>Conclusion</h2>
<p>
All three frameworks successfully orchestrated the same ETL pipeline
and produced identical outputs.
</p>

<p>
The real difference lies in <strong>developer experience</strong>,
<strong>setup complexity</strong>, and <strong>execution philosophy</strong>.
</p>

<p>
Choosing an orchestrator is less about features and more about
<strong>team needs</strong>, <strong>infrastructure maturity</strong>,
and <strong>development workflow</strong>.
</p>
