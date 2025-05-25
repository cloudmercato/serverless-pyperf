build_aws_lambda:
	docker build \
		-f aws-lambda/Dockerfile \
		--provenance=false \
		-t pyperf-lambda

run_aws_lambda:
	docker run -p 9000:8080 pyperf-lambda

package_aws_lambda:
	cd aws-lambda && ./make_zip.sh

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

run_scw_function:
	python scw/app.py

fire_scw_function:
	curl "http://localhost:8080/" -d '{"benchmarks": ["2to3"]}'

push_azure_function:
	cd azure-functions && \
		az functionapp create --resource-group default-eastus --consumption-plan-location eastus --runtime python --runtime-version 3.12 --functions-version 4 --name pyperf --storage-account osbeastussl --os-type Linux
