from fastapi import FastAPI, HTTPException

# Membuat instance dari FastAPI
app = FastAPI()

# Endpoint root
@app.get('/')
async def root():
    return [
        {"id": 1, "nama": "Endpoint User", "endpoint": "/user"},
        {"id": 2, "nama": "Endpoint User Detail", "endpoint": "/user/user_detail"},
        {"id": 3, "nama": "Endpoint Doswal", "endpoint": "/doswal"},
        {"id": 4, "nama": "Endpoint Praktikum", "endpoint": "/praktikum"},
        {"id": 5, "nama": "Endpoint Matkul", "endpoint": "/matkul"},
    ]

# Data dummy untuk users
users = [
    {
        "id": 1, 
        "nama": "Seva Giantama Farel", 
        "nim": "123210061",
        "hobby": "Reading",
        "umur": 21,
        "motto_hidup": "Never stop learning."
    },
    {
        "id": 2, 
        "nama": "Muhammad Raditya Haikal Mumtaz", 
        "nim": "123210062",
        "hobby": "Cycling",
        "umur": 22,
        "motto_hidup": "Live life to the fullest."
    },
    {
        "id": 3, 
        "nama": "Alfin Shalahuddin Ahmad", 
        "nim": "123210079",
        "hobby": "Gaming",
        "umur": 23,
        "motto_hidup": "Stay positive, work hard, make it happen."
    },
]

# Endpoint untuk mendapatkan data user
@app.get('/user')
async def user_data():
    # Menyederhanakan data user agar hanya mengandung id, nama, dan nim
    simplified_users = [
        {"id": user["id"], "nama": user["nama"], "nim": user["nim"]}
        for user in users
    ]
    return {
        "Message": "Success fetch user data",
        "Data": simplified_users
    }

# Endpoint untuk mendapatkan detail user berdasarkan id
@app.get('/user/{user_id}')
async def user_detail(user_id: int):
    # Mencari user berdasarkan id
    for user in users:
        if user["id"] == user_id:
            return {
                "Message": "Success fetch user detail",
                "Data": user
            }
    # Jika user tidak ditemukan, mengembalikan HTTP 404
    raise HTTPException(status_code=404, detail="User not found")

# Endpoint untuk mendapatkan data doswal
@app.get('/doswal')
async def doswal_data():
    # Data dummy doswal
    return {
        "Message": "Success fetch doswal data",
        "Data": [
            {"id": 1, "nama": "Bu Herlina"},
            {"id": 2, "nama": "Pak Rifki"},
            {"id": 3, "nama": "Pak Heriyanto"},
        ]    
    }

# Endpoint untuk mendapatkan data praktikum
@app.get('/praktikum')
async def praktikum_data():
    # Data dummy praktikum
    return {
        "Message": "Success fetch praktikum data",
        "Data": [
            {"id": 1, "praktikum": "Praktikum TCC"},
            {"id": 2, "praktikum": "Praktikum TPM"},
            {"id": 3, "praktikum": "Praktikum IoT"},
        ]    
    }

# Endpoint untuk mendapatkan data matkul
@app.get('/matkul')
async def matkul_data():
    # Data dummy matkul
    return {
        "Message": "Success fetch matkul data",
        "Data": [
            {"id": 1, "matkul": "Grafika Komputer", "dosen": "Pak Kodong"},
            {"id": 2, "matkul": "Teknologi Cloud Computing", "dosen": "Pak Awang & Pak Andiko"},
            {"id": 3, "matkul": "Teknologi dan Pemrograman Mobile", "dosen": "Pak Bagus & Pak Sutiyo"},
        ]
    }
