import os

def main():
    workflow_name = os.getenv('GITHUB_EVENT_NAME')
    print(f"The {workflow_name} workflow completed successfully.")
    # Add your additional status check logic here

if __name__ == "__main__":
    main()
