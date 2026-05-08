import sys
from databricks.sdk import WorkspaceClient
from databricks.sdk.service.jobs import Task, NotebookTask, Source

# 1. Version Check
current_version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
print(f"Current Python Version: {current_version}")
print(" Python Version 3.11.6 confirmed.") if current_version == "3.11.6" else print(" Version Mismatch")

# 2. Workspace Client Initialization
w = WorkspaceClient(
    host="https://dbc-eca9a387-3473.cloud.databricks.com",
    token="dapib4e161127cec6da4ae630f2dd97cfce0"
)

def run_notebook(notebook_path, task_name):
    print(f" Running: {task_name}...")
    try:
        # Serverless Job Submit
        run = w.jobs.submit(
            run_name=f"Pipeline_{task_name}",
            tasks=[
                Task(
                    task_key=task_name,
                    notebook_task=NotebookTask(
                        notebook_path=notebook_path,
                        source=Source.WORKSPACE
                    )
                )
            ]
        ).result()
        print(f" {task_name} Completed.")
    except Exception as e:
        print(f" {task_name} Failed: {e}")
        raise e

print("\n---  Medallion Pipeline Orchestration Started ---")


BASE_PATH = "/Users/aungbobohtwenex4@gmail.com"

try:
    # 1။ Bronze Layer
    run_notebook(f"{BASE_PATH}/01_Bronze_Layer", "Bronze_Layer")

    # 2။ Silver Layer
    run_notebook(f"{BASE_PATH}/Silver_Process_Masking", "Silver_Layer")

    # 3။ Gold Layer
    run_notebook(f"{BASE_PATH}/03_Gold_Layer", "Gold_Layer")

    print("\n---  ALL PIPELINE STAGES COMPLETED SUCCESSFULLY  ---")

except Exception:
    print("\n Pipeline stopped due to error.")