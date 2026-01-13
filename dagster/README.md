<h1>Dagster Implementation</h1>



<h2>Overview</h2>

<p>

This directory contains the <strong>Dagster</strong> implementation of the shared ETL pipeline.

Dagster emphasizes <strong>explicit execution</strong>, <strong>strong structure</strong>,

and a clear separation between pipeline definition and execution.

</p>



<p>

All ETL business logic is imported from the shared module.

Dagster is responsible for defining and executing the pipeline in a predictable,

explicit manner.

</p>



<h2>Prerequisites</h2>

<ul>

&nbsp;   <li>Python <strong>3.10</strong></li>

&nbsp;   <li>Virtual environment (recommended)</li>

</ul>



<h2>Setup Instructions</h2>



<p>From the project root (inside an active virtual environment):</p>



<pre>

pip install dagster dagster-webserver pandas pyarrow

</pre>



<h2>Running the Pipeline</h2>



<p>From the <code>dagster/</code> directory:</p>



<pre>

python dagster\_job.py

</pre>



<p>

This explicitly executes the Dagster job using

<code>execute\_in\_process()</code>.

</p>



<h3>Output File</h3>

<pre>

data/dagster\_output.parquet

</pre>



<div class="highlight">

Dagster does <strong>not</strong> implicitly run jobs.

Execution is an explicit action, not a side effect.

</div>



<h2>Optional UI</h2>



<p>

To launch the Dagster development UI:

</p>



<pre>

dagster dev

</pre>



<p>Then open:</p>



<pre>

http://localhost:3000

</pre>



<h2>Retry Behavior</h2>



<ul>

&nbsp;   <li>Retries are configured via <code>RetryPolicy</code></li>

&nbsp;   <li>The transform op retries up to <strong>2 times</strong></li>

</ul>



<div class="note">

Retry behavior is explicit and attached directly to ops,

making execution behavior easy to reason about.

</div>



<h2>Notes</h2>



<ul>

&nbsp;   <li>Jobs must be <strong>explicitly executed</strong></li>

&nbsp;   <li>No hidden scheduling or implicit runs</li>

&nbsp;   <li>Strong structure encourages correctness over convenience</li>

</ul>



<h2>Design Intent</h2>

<p>

This implementation highlights Dagster’s role as a

<strong>middle ground</strong> between Airflow and Prefect.

</p>



<p>

Dagster provides more structure and predictability than Prefect,

without the operational overhead and state complexity of Airflow,

while still producing identical outputs.

</p>





