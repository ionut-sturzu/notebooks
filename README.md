#Agent workflow notebook

This notebook creates an agent workflow setup using Llama3 as main agent, CodeLlama as code model and CuOpt as optimization model.
It will spin up a Gradio interface for an easy way to interact with the model.

If using our automation to deploy the models, the to run this notebook you will need to follow the bellow steps:
1. Run the first cell to install the required python packages.
2. Run the code cell. 

If you are deploying models in a different way you will need to change the links to API for each model:
```
agent_base_url = "http://llama3/v1"
code_base_url = "http://codellama/v1"
optimization_base_url = "http://cuopt-cuopt-deployment-cuopt-service:5000/cuopt/routes"
```