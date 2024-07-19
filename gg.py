import argparse
import webbrowser

def main():
    parser = argparse.ArgumentParser(description="Redirect to a Discord invite URL.")
    parser.add_argument('-Direct', type=str, required=True, help="Discord invite code")
    
    args = parser.parse_args()
    
    discord_code = args.Direct
    discord_url = f"https://discord.gg/{discord_code}"
    
    print(f"Redirecting to: {discord_url}")
    webbrowser.open(discord_url)

if __name__ == "__main__":
    main()
