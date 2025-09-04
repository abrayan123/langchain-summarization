# from utils.env_loader import load_env_vars
from utils.env_loader import load_env_vars

def main():
    creds = load_env_vars()
    print("Environment Variables Loaded:")
    for key, value in creds.items():
        masked = value[:5] + "..." if value else "Not Found"
        print(f"{key}: {masked}")

if __name__ == "__main__":
    main()
