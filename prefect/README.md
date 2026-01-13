<h1>Prefect Implementation</h1>



<h2>Overview</h2>

<p>

This directory contains the <strong>Prefect</strong> implementation of the shared ETL pipeline.

Prefect provides a <strong>Python-first execution model</strong> with minimal boilerplate,

allowing pipelines to be written, executed, and debugged like normal Python programs.

</p>



<p>

All ETL business logic is imported from the shared module.

Prefect is used purely to orchestrate execution and retries.

</p>



<h2>Prerequisites</h2>

<ul>

&nbsp;   <li>Python <strong>3.10</strong></li>

&nbsp;   <li>Virtual environment (recommended)</li>

</ul>



<h2>Setup Instructions</h2>



<p>From the project root:</p>



<pre>

python -m venv .venv

.venv\\Scripts\\activate

pip install "prefect\&lt;3" pandas pyarrow

</pre>



<div class="note">

Prefect <strong>2.x</strong> is intentionally pinned.

Prefect 3.x introduces breaking changes that are not compatible with this implementation.

</div>



<h2>Running the Pipeline</h2>



<p>From the <code>prefect/</code> directory:</p>



<pre>

python prefect\_flow.py

</pre>



<h3>Output File</h3>

<pre>

data/prefect\_output.parquet

</pre>



<h2>Retry Behavior</h2>



<ul>

&nbsp;   <li>Retries are defined directly on Prefect tasks</li>

&nbsp;   <li>The transform task retries up to <strong>2 times</strong></li>

&nbsp;   <li>Retry delay is <strong>10 seconds</strong></li>

</ul>



<div class="highlight">

Retry logic is explicit, readable, and colocated with task definitions.

No external state clearing or manual intervention is required.

</div>



<h2>Notes</h2>



<ul>

&nbsp;   <li>Prefect supports <strong>in-memory data passing</strong> between tasks</li>

&nbsp;   <li>No external database or scheduler is required for local execution</li>

&nbsp;   <li>Pipelines can be debugged using standard Python tools</li>

&nbsp;   <li>Version pinning is critical for stability</li>

</ul>



<h2>Design Intent</h2>

<p>

This implementation highlights Prefect’s strengths in

<strong>developer ergonomics</strong>, <strong>fast iteration</strong>,

and <strong>low setup overhead</strong>.

</p>



<p>

The goal is to contrast Prefect’s execution model with

Airflow’s state-heavy orchestration and Dagster’s explicit job model

while producing identical outputs.

</p>





