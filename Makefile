build_aws_lambda:
	docker build \
		-f aws-lambda/Dockerfile \
		--provenance=false \
		-t pyperf-lambda

run_aws_lambda:
	docker run -p 9000:8080 pyperf-lambda

fire_aws_lambda:
	curl "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"benchmarks": ["2to3"]}'

run_gc_run_function:
	cd gc-run-function && functions-framework --target handler

fire_gc_run_function:
	curl "http://localhost:8080" -H "Content-Type:application/json" -d '{"benchmarks": ["2to3"]}'

build_oracle_function:
	fn build oracle-functions

run_oracle_function:
	fn start oracle-functions
