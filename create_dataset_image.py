import os
import urllib.request

# Dizionario degli URL delle immagini per i 15 piatti
FOOD_IMAGE_URLS = {
    "tiramisu": [
        "https://images.unsplash.com/photo-1571877227200-a0d98ea607e9?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8dGlyYW1pcyVDMyVCOXxlbnwwfHwwfHx8Mg%3D%3D",
        "https://images.unsplash.com/photo-1639744211487-b27e3551b07c?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8dGlyYW1pcyVDMyVCOXxlbnwwfHwwfHx8Mg%3D%3D"
    ],
    "pizza": [
        "https://images.unsplash.com/photo-1574071318508-1cdbab80d002?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Nnx8cGl6emF8ZW58MHx8MHx8fDI%3D",
        "https://images.unsplash.com/photo-1628840042765-356cda07504e?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTB8fHBpenphfGVufDB8fDB8fHwy"
    ],
    "baklava": [
        "https://images.unsplash.com/photo-1617806501553-d3a6a3a7b227?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8YmFrbGF2YXxlbnwwfHwwfHx8Mg%3D%3D",
        "https://images.unsplash.com/photo-1651493829690-ccad11ee95fa?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8N3x8YmFrbGF2YXxlbnwwfHwwfHx8Mg%3D%3D"
    ],
    "churros": [
        "https://images.unsplash.com/photo-1615915848347-5ad361d3e9fd?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8Y2h1cnJvc3xlbnwwfHwwfHx8Mg%3D%3D",
        "https://images.unsplash.com/photo-1624371414361-e670edf4898d?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8Y2h1cnJvc3xlbnwwfHwwfHx8Mg%3D%3D"
    ],
    "sushi": [
        "https://images.unsplash.com/photo-1579871494447-9811cf80d66c?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8c3VzaGl8ZW58MHx8MHx8fDI%3D",
        "https://images.unsplash.com/photo-1563612116625-3012372fccce?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OXx8c3VzaGl8ZW58MHx8MHx8fDI%3D"
    ],
    "caprese_salad": [
        "https://images.unsplash.com/photo-1595587870672-c79b47875c6a?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8Y2FwcmVzZSUyMHNhbGFkfGVufDB8fDB8fHwy",
        "https://images.unsplash.com/photo-1610817153377-e54299ffdb1e?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8Y2FwcmVzZSUyMHNhbGFkfGVufDB8fDB8fHwy"
    ],
    "guacamole": [
        "https://images.unsplash.com/photo-1595016111459-799a195e7452?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8Z3VhY2Ftb2xlfGVufDB8fDB8fHwy",
        "https://images.unsplash.com/photo-1620019989549-bbb873b6612d?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8Z3VhY2Ftb2xlfGVufDB8fDB8fHwy"
    ],
    "paella": [
        "https://images.unsplash.com/photo-1630175860333-5131bda75071?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8cGFlbGxhfGVufDB8fDB8fHwy",
        "https://images.unsplash.com/photo-1650964802649-ef992b574b8c?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8N3x8cGFlbGxhfGVufDB8fDB8fHwy"
    ],
    "ramen": [
        "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8cmFtZW4lMjBub29kbGVzfGVufDB8fDB8fHwy",
        "https://images.unsplash.com/photo-1612927601601-6638404737ce?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8cmFtZW4lMjBub29kbGVzfGVufDB8fDB8fHwy"
    ],
    "pancakes": [
        "https://images.unsplash.com/photo-1612182062633-9ff3b3598e96?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8cGFuY2FrZXN8ZW58MHx8MHx8fDI%3D",
        "https://images.unsplash.com/photo-1587339144367-f1cacbecac82?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8cGFuY2FrZXN8ZW58MHx8MHx8fDI%3D"
    ],
    "falafel": [
        "https://images.unsplash.com/photo-1593001874117-c99c800e3eb8?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8N3x8ZmFsYWZlbHxlbnwwfHwwfHx8Mg%3D%3D",
        "https://images.unsplash.com/photo-1593001867410-22f463e592ed?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OXx8ZmFsYWZlbHxlbnwwfHwwfHx8Mg%3D%3D"
    ],
    "ice_cream": [
        "https://images.unsplash.com/photo-1497034825429-c343d7c6a68f?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8aWNlJTIwY3JlYW18ZW58MHx8MHx8fDI%3D",
        "https://images.unsplash.com/photo-1718810125230-e8e2271354f5?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    ],
    "crepes": [
        "https://images.unsplash.com/photo-1519676867240-f03562e64548?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Y3JlcGVzfGVufDB8fDB8fHwy",
        "https://images.unsplash.com/photo-1665105649617-69dbcf320456?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTJ8fGNyZXBlc3xlbnwwfHwwfHx8Mg%3D%3D"
    ],
    "hamburger": [
        "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8aGFtYnVyZ2VyfGVufDB8fDB8fHwy",
        "https://images.unsplash.com/photo-1572802419224-296b0aeee0d9?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8aGFtYnVyZ2VyfGVufDB8fDB8fHwy"
    ],
    "croissant": [
        "https://images.unsplash.com/photo-1691480162735-9b91238080f6?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Y3JvaXNzYW50c3xlbnwwfHwwfHx8Mg%3D%3D",
        "https://images.unsplash.com/photo-1599940778173-e276d4acb2bb?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8Y3JvaXNzYW50c3xlbnwwfHwwfHx8Mg%3D%3D"
    ]
}

def create_mini_dataset(base_dir="."):
    """Crea le cartelle dei piatti direttamente nella directory corrente del progetto in VS Code."""
    headers = {'User-Agent': 'Mozilla/5.0'}

    print("--- SCARICAMENTO IMMAGINI NELLA CARTELLA PRINCIPALE DI VS CODE ---")
    for food_name, urls in FOOD_IMAGE_URLS.items():
        food_dir = os.path.join(base_dir, food_name)
        os.makedirs(food_dir, exist_ok=True)
        
        for i, url in enumerate(urls):
            file_path = os.path.join(food_dir, f"{food_name}_{i+1}.jpg")
            if not os.path.exists(file_path):
                req = urllib.request.Request(url, headers=headers)
                try:
                    with urllib.request.urlopen(req) as response, open(file_path, 'wb') as out_file:
                        out_file.write(response.read())
                    print(f"✓ Scaricata: {file_path}")
                except Exception as e:
                    print(f"x Errore scaricando {url}: {e}")
            else:
                print(f"Già presente: {file_path}")

    print("\n✓ Cartelle dei piatti create con successo direttamente nel tuo progetto VS Code!")

if __name__ == "__main__":
    create_mini_dataset()